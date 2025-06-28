from fastapi import FastAPI, UploadFile
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from local setup!"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    img_bytes = image.file.read()
    img = Image.open(io.BytesIO(img_bytes))
    # Call your model pipeline here:
    # result = model_pipeline(text, img)
    result = "Dummy response"  # Replace with real result
    return {"answer": result}
