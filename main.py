from fastapi import FastAPI
import platform
import os
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "name": "Muathaf Cloud Deployment",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "python": platform.python_version(),
        "system": platform.system(),
        "hostname": os.uname().nodename,
    }