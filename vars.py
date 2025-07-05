#King
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22727211"))
API_HASH = environ.get("API_HASH", "bf39e58d7901555ef26f8390e9b8e380")
BOT_TOKEN = environ.get("BOT_TOKEN", "7102187991:AAFDJKu3Y55SgrVCEflUHP5GYq1I46F9uac")
OWNER = int(environ.get("OWNER", "6402213602"))
CREDIT = "King"
AUTH_USER = os.environ.get('AUTH_USERS', '6402213602').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
