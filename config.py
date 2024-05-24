import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23144161"))
API_HASH = getenv("API_HASH", "0e156557bde6def9a8541cc8c65d57df")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6723540039:AAEFLVL2lJ7_uLjrI13_rtJNnVR1QfPNfGE")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002125936547"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6563936773))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "music06")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-7a607b1b-0b00-4c2d-a664-2a481499b4d7")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Rq7mg/k-y-c-music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kycmusicdestek")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kiyicitayfaa")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFhJuEAC7VFTVdMJzX9aMctOEpgzhoS9jsj37U_UqlbLf_3kXfVmbp0OaIOyaXbo0neh-ZYiJVWb2vXwbWy-AaRPKyJ-hYFPlP5svNe4wSCI4Q-osl9Fg1c9hQZ4uz3bwdlQGMVHRxhS92iQ8FHdFHltUWtntKFUlcc2CN-7a1UGIS4a-BZyzPIuD477vDZqeZjs2oO6ZbGXY1HqX_QHw9oHCDrRFViM0RHoufqJFtsAD_N4kFXCVvtARiS9cuiyMXph-yNFzZOIHJop9irZtS7BP2i6rt_Y9pw0vF9f4aXenpizhP1A5QYtls8OAR8-PAUkBIhqjnlUvDtYVN-YPviJCdDfAAAAAGcKU3CAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/resim-03-14"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/resim-03-14"
)
PLAYLIST_IMG_URL = "https://telegra.ph/resim-03-14"
STATS_IMG_URL = "https://telegra.ph/resim-03-14"
TELEGRAM_AUDIO_URL = "https://telegra.ph/resim-03-14"
TELEGRAM_VIDEO_URL = "https://telegra.ph/resim-03-14"
STREAM_IMG_URL = "https://telegra.ph/resim-03-14"
SOUNCLOUD_IMG_URL = "https://telegra.ph/resim-03-14"
YOUTUBE_IMG_URL = "https://telegra.ph/resim-03-14"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/resim-03-14"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/resim-03-14"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/resim-03-14"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
