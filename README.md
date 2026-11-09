# 🎭 Joke Trainer

Write jokes, get AI-powered feedback — works with local LLMs (LM Studio, Ollama) and cloud APIs (OpenRouter, Groq, NVIDIA NIM).

**Try it live:** https://drobin04.github.io/joke-trainer/

## Quick Start (local)

```bash
cd joke-trainer
./serve.sh
```

Open **http://localhost:8080** in your browser.

## How to Use

1. **Pick a provider** in the settings bar — Local, OpenRouter, Groq, NVIDIA NIM, or Custom.
2. **Add an API key** if using a cloud provider (free tiers available — no credit card needed).
3. **Generate a premise** — choose Short (broad topic) or Elaborate (detailed scenario).
4. **Write your joke** in the text area — you can also edit the premise box directly.
5. **Evaluate** — get a score /10, detailed analysis, and specific tips to improve.

## Providers

| Provider | Default Model | Key Required |
|---|---|---|
| Local (LM Studio) | Uses loaded model | No |
| OpenRouter | `openrouter/free` | Yes (free at openrouter.ai/keys) |
| Groq | `llama-3.3-70b-versatile` | Yes (free at console.groq.com) |
| NVIDIA NIM | `deepseek-ai/deepseek-v4.1-flash` | Yes (free at build.nvidia.com) |
| Custom URL | User-defined | Optional |

## Running

**Locally with proxy** (recommended — works with all backends including local):
```bash
./serve.sh
# or: python3 server.py
```
Then open http://localhost:8080.

**GitHub Pages** (cloud providers only):
Open https://drobin04.github.io/joke-trainer/ — the app falls back to direct API calls when the local proxy isn't available.

## Files

| File | Purpose |
|---|---|
| `index.html` | The web app (standalone, no build step) |
| `server.py` | Python proxy server (optional — for local/LAN backends) |
| `serve.sh` | Shortcut — runs `server.py` |

## Requirements

- **Local mode:** Python 3 + LM Studio or Ollama
- **Cloud mode:** A browser and free API keys from your chosen provider