from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
import logging
from datetime import datetime, timezone

app = FastAPI(title="Profile + Cat Facts API")

# --------------------------
# Logging Configuration
# --------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()  # also logs to console (Railway captures this)
    ]
)
logger = logging.getLogger(__name__)

# --------------------------
# Static User Information
# --------------------------
USER_INFO = {
    "email": "nbinael@yahoo.com",
    "name": "Binael Nchekwube",
    "stack": "Python/FastAPI"
}

# --------------------------
# External API Endpoint
# --------------------------
CAT_FACTS_URL = "https://catfact.ninja/fact"


@app.get("/me", response_class=JSONResponse)
async def get_profile():
    """
    Returns user profile information with a random cat fact.
    """
    logger.info("Received request to /me endpoint")

    # Fetch random cat fact from external API
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            logger.info(f"Fetching cat fact from {CAT_FACTS_URL}")
            response = await client.get(CAT_FACTS_URL)
            response.raise_for_status()
            cat_fact_data = response.json()
            cat_fact = cat_fact_data.get("fact", "Cats are amazing creatures!")
            logger.info("Successfully fetched cat fact")
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Could not fetch cat fact at the moment. Try again later."

    # Generate current UTC timestamp
    timestamp = datetime.now(timezone.utc).isoformat()

    result = {
        "status": "success",
        "user": USER_INFO,
        "timestamp": timestamp,
        "fact": cat_fact,
    }

    logger.info("Returning /me response successfully")
    return JSONResponse(content=result, media_type="application/json")
