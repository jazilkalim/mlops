import nest_asyncio
from pyngrok import ngrok
import uvicorn
import os
os.environ["NGROK_PATH"] = "C:\\Users\\afiniti\\ngrok-v3-stable-windows-amd64\\ngrok.exe"

ngrok.set_auth_token("2vbcyj0GFQXW3fcO1YScPSpZ868_5fc4jBsGaWWcyRp7f5dSA")
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

nest_asyncio.apply()
uvicorn.run("app:app", host="0.0.0.0", port=8000)
