#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27607585"))
API_HASH = environ.get("API_HASH", "725f60b51e233703576199334610011a")
BOT_TOKEN = environ.get("BOT_TOKEN", "8495221315:AAF9Q6qXOYiaKWQExCQU1U6Qwry75hF0jqI")

OWNER = int(environ.get("OWNER", "5666930893"))
CREDIT = environ.get("CREDIT", "KANHA 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5666930893').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5666930893').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

