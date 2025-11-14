from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from PIL import Image
import pytesseract
import io
import os

app = FastAPI(title="Paste OCR service")

# Allow local frontend. In production restrict origins appropriately.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html explicitly at root and static files at /static


@app.get("/")
async def index():
    return FileResponse(os.path.join("static", "index.html"))

app.mount("/static", StaticFiles(directory="static"), name="static")


class OCRResponse(BaseModel):
    text: str


@app.post("/ocr", response_model=OCRResponse)
async def ocr(file: UploadFile = File(...)):
    """
    Accepts an image file and returns OCR text.
    """
    # Basic validation
    if not file.content_type or file.content_type.split("/")[0] != "image":
        return {"text": ""}

    contents = await file.read()
    try:
        image = Image.open(io.BytesIO(contents))
    except Exception:
        return {"text": ""}

    # Use pytesseract (requires system tesseract binary)
    text = pytesseract.image_to_string(image)

    return {"text": text}
