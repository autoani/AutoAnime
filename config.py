from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 17894641))
API_HASH = getenv("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
BOT_TOKEN = getenv("BOT_TOKEN", "5844583505:AAEEvbpS4Ge7nIglVAmLHX0T4pdLHBsFWfI")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://autoani:autoani@autoani.enmf46d.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("INDEX_ID", -1001858537966))
UPLOADS_ID = int(getenv("UPLOADS_ID", -1001521731149))

STATUS_ID = int(getenv("STATUS_ID", 6))
SCHEDULE_ID = int(getenv("SCHEDULE_ID", 7))

CHANNEL_TITLE = getenv("CHANNEL_TITLE", "UTUAnimePahe")
INDEX_USERNAME = getenv("INDEX_USERNAME", "UTUindex")
UPLOADS_USERNAME = getenv("UPLOADS_USERNAME", "UTUUpload")
