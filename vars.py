#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20699247"))
API_HASH = environ.get("API_HASH", "a1271e4ecc86745a62d222b62be8ba96")
BOT_TOKEN = environ.get("BOT_TOKEN", "8146132788:AAHm2sWlzBWFFBUKIidZKHyTuY-FchAZw4g")

OWNER = int(environ.get("OWNER", "1543124151"))
CREDIT = environ.get("CREDIT", "NAYAK BOTS")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5666930893').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5666930893').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


