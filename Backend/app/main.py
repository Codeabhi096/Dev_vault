from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Developer Knowledge Management Platform",
    version="0.1.0",
    debug=settings.debug
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": f"{settings.app_name} API is running"
    }