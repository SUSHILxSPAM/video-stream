import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "SUSHIL")
ALIVE_NAME = getenv("ALIVE_NAME", "COBRA")
BOT_USERNAME = getenv("BOT_USERNAME", "Rockerz_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Cobra_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "X8_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "welcomefriendclub")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/video-stream")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/85954f386aa7195ef3dc4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/85954f386aa7195ef3dc4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/85954f386aa7195ef3dc4.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/85954f386aa7195ef3dc4.jpg")
