# google-adk-projects

Minimal [Google ADK](https://google.github.io/adk-docs/) experiments. Start with **`simple_agent`**: OpenAI via ADK’s **LiteLLM** integration (`LiteLlm`), no extra tools.

## Setup (Windows PowerShell)

```powershell
cd google-adk-projects
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item simple_agent\.env.example simple_agent\.env
```

Edit `simple_agent\.env` and set **`OPENAI_API_KEY`** from [OpenAI API keys](https://platform.openai.com/api-keys). Optionally set **`OPENAI_MODEL`** (default `gpt-4o-mini`; LiteLLM uses ids like `openai/gpt-4o-mini`).

`google-adk[extensions]` pulls in LiteLLM support used by `LiteLlm`.

## Run

Stay in the **`google-adk-projects`** directory (parent of `simple_agent/`):

```powershell
adk run simple_agent
```

If `adk` is not on your PATH:

```powershell
python -m google.adk.cli run simple_agent
```

### Web UI (dev only)

```powershell
adk web --port 8000
```

Open the URL shown, pick **`simple_agent`** in the UI, and chat.
