# Image Resize 🖼️🔧

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-3.1.2-000000.svg?logo=flask)](https://palletsprojects.com/p/flask/) [![Pillow](https://img.shields.io/badge/Pillow-12.1.0-ff69b4.svg?logo=python)](https://python-pillow.org/) [![Requirements](https://img.shields.io/badge/requirements-requirements.txt-%23009688)](requirements.txt) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

A tiny Flask app that resizes and optimizes images (JPEG / PNG) via a simple web form or a single HTTP request.

---

## 🚀 Quick overview

- **Built with:** Flask + Pillow
- **Purpose:** Upload an image, optionally specify width, height and quality, then download an optimized, resized copy.

---

## ✅ Features

- Web UI for uploading and resizing images
- Preserves PNG format, otherwise saves as JPEG
- Optional `quality` parameter (defaults to 85)
- Downloads optimized file as `opt_<original_filename>`

---

## 🔧 Requirements

- **Python 3.10+** (this project uses a venv for Python 3.10.11)
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Packages included (from `requirements.txt`):
- Flask
- Pillow
- Jinja2
- and other basic utilities

---

## 🏁 Quick start (Windows)

1. Create a virtual environment (if you don't already have one):

```powershell
python -m venv env
```

2. Activate it (PowerShell):

```powershell
.\env\Scripts\Activate.ps1
```

Or (cmd.exe):

```cmd
.\env\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python run.py
```

5. Open your browser to:

```
http://127.0.0.1:5000
```

---

## 🧪 Usage

Web UI: open the page, choose an image and optionally set **Width**, **Height**, and **Quality**, then submit. If both width and height are provided, the image will be resized to those exact dimensions.

Curl example (automated usage):

```bash
curl -X POST \
  -F "image=@/path/to/image.jpg" \
  -F "width=800" \
  -F "height=600" \
  -F "quality=80" \
  http://127.0.0.1:5000 -o opt_image.jpg
```

Notes:
- `width` and `height` must be integers. If omitted, the image will not be resized (but will be re-saved/optimized).
- `quality` is an integer (1-100). Default is **85** (applies to JPEG output).
- Output filename will be `opt_<original_filename>`.

---

## ⚠️ Implementation details / gotchas

- The app determines output format: if the uploaded image is PNG it saves as PNG; otherwise saves as JPEG.
- If you need different behavior (preserve exact format or handle other formats), modify `run.py`.
- If port 5000 is occupied, change the port by editing `run.py` or running behind a production server.

> Tip: To enable Flask debug mode while testing, either edit `run.py` to `app.run(debug=True)` or set the appropriate environment variables prior to running.

---

## 🧩 Project structure (relevant files)

- `run.py` — Flask app (entry point)
- `requirements.txt` — Python dependencies
- `templates/index.html` — simple upload UI
- `env/` — local virtual environment (not needed in source; included for reference)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---
