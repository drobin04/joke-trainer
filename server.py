#!/usr/bin/env python3
"""
Joke Trainer Server
Serves the frontend and proxies API calls to the configured LM Studio backend,
bypassing CORS restrictions when the backend is on a different machine.
"""

import json
import os
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

HOST = '0.0.0.0'
PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):

    # ── CORS ────────────────────────────────────────────────────────────
    def _cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    # ── Proxy ───────────────────────────────────────────────────────────
    def do_POST(self):
        if self.path != '/api/proxy':
            self.send_error(404)
            return

        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length)
        data = json.loads(raw) if raw else {}

        target = data.get('target', 'http://localhost:1234').rstrip('/')
        path   = data.get('path', '/v1/chat/completions')
        method = data.get('method', 'POST')
        req_body = data.get('body')
        req_headers = data.get('headers', {})

        url = target + path
        req = urllib.request.Request(url, method=method)
        req.add_header('Content-Type', 'application/json')
        for key, value in req_headers.items():
            req.add_header(key, value)

        if req_body is not None:
            req.data = json.dumps(req_body).encode('utf-8')

        try:
            resp = urllib.request.urlopen(req, timeout=1200)
            resp_body = resp.read()
            self.send_response(resp.status)
            self._cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(resp_body)
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self._cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(502)
            self._cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))

    def do_GET(self):
        # Serve static files (defaults to index.html)
        return super().do_GET()

    def translate_path(self, path):
        if path == '/':
            path = '/index.html'
        return super().translate_path(path)


if __name__ == '__main__':
    os.chdir(DIR)
    sv = HTTPServer((HOST, PORT), Handler)
    print(f'→ Joke Trainer  http://localhost:{PORT}')
    print(f'  (proxies API calls to your configured LM Studio backend)')
    try:
        sv.serve_forever()
    except KeyboardInterrupt:
        sv.shutdown()
        print('\n  stopped')