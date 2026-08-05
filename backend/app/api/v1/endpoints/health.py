from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health", tags = ["Health"])
def health_check():
    """
    Health check endpoint to verify if the API is running.
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
        "message": "AI Workspace API is running successfully."
    }