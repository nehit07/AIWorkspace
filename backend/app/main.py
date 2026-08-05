import logging

from fastapi import FastAPI

from app.api.v1.api import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging

logger = logging.getLogger(__name__)

# Configure application logging
setup_logging()

logger.info(
    f"Starting {settings.APP_NAME} (version: {settings.APP_VERSION}) in {settings.APP_ENV} environment."
)

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG
)

app.include_router(api_router, prefix="/api/v1", tags=["API"])
