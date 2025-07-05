#Shaitan
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27326129"))
API_HASH = environ.get("API_HASH", "896c2bd70f1d1101c3f35290b2a83546")
BOT_TOKEN = environ.get("BOT_TOKEN", "8093395647:AAHLNfDP4Q8w1oVbM4GybUlLCYsA1X7tXJI")
OWNER = int(environ.get("OWNER", "6402213602"))
CREDIT = "*𝐒нɑᎥ𝚝ɑη*"
AUTH_USER = os.environ.get('AUTH_USERS', '6402213602').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
