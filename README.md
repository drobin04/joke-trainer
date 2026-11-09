# 🎭 Joke Trainer

Write jokes, get AI-powered feedback — works with any OpenAI-compatible local LLM (LM Studio, Ollama, etc.).

## Quick Start

```bash
cd joke-trainer
./serve.sh
```

Open **http://localhost:8080** in your browser.

## How to Use

1. **Make sure your LLM is running** — LM Studio, Ollama, or any OpenAI-compatible server.
2. **Set the backend URL** in the top bar of the app (default: `http://localhost:1234`).
3. **Generate a premise** — click the button to get a random joke scenario.
4. **Write your joke** in the text area.
5. **Evaluate** — get a score, detailed breakdown, and specific tips to improve.

## Backend URLs

| Service | Default URL |
|---|---|
| LM Studio | http://localhost:1234 |
| Ollama | http://localhost:11434 |
| Remote server | http://192.168.x.x:1234 |

The app proxies all API calls through the local server to avoid CORS issues, so remote/ LAN backends work too.

## Files

| File | Purpose |
|---|---|
| `index.html` | The web app — open via the server, not directly from `file://` |
| `server.py` | Python proxy server that serves the app and forwards API calls |
| `serve.sh` | Shortcut — runs `server.py` |
| `README.md` | This file |

## Requirements

- Python 3 (pre-installed on most systems)
- A running local LLM server (e.g. LM Studio)