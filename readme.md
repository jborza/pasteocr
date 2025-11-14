```markdown
# Simple Paste-to-OCR (FastAPI + vanilla JS)

Overview
- Small FastAPI backend that accepts pasted/uploaded images and returns OCR text.
- Frontend: a single HTML page that supports paste from clipboard and file input.

Prerequisites
- Python 3.8+
- Install the Tesseract binary on the host:
  - Debian/Ubuntu: sudo apt-get update && sudo apt-get install -y tesseract-ocr
  - macOS (Homebrew): brew install tesseract
  - Windows: download installer from https://github.com/tesseract-ocr/tesseract
- Create and activate a Python venv and install Python deps:
  python -m venv .venv
  source .venv/bin/activate    # or .venv\\Scripts\\activate on Windows
  pip install -r requirements.txt

Run locally
- Start the API:
  uvicorn main:app --reload --host 127.0.0.1 --port 8000
- Open the static `index.html` (served via a simple file open or a static server) — or point browser to where you serve it.

Docker (optional)
- If you want everything in one container, use the provided Dockerfile (it installs tesseract in the image).

Security & production
- Limit upload sizes (e.g. via nginx or middleware).
- Restrict CORS origins.
- Add authentication if needed.
- Use a worker queue for heavy loads.

```