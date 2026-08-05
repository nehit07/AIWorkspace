from fastapi import FastAPI
from app.api.v1.api import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging

# Configure application logging
setup_logging()

# Create FastAPI application
app = FastAPI(
    title = settings.APP_NAME,
    version = settings.APP_VERSION,
    debug = settings.DEBUG
)

app.include_router(
    api_router,
    prefix = "/api/v1",
    tags = ["API"]
)