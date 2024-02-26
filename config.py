from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f8995139e4f503955150b.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f8995139e4f503955150b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/darMahd313")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/darMahd313")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5695872306").split()))


CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO", "darMahd313"
)

YAFA_NAME = getenv(
    "YAFA_NAME", "دار الاحــرار 313 💚"
)

YAFA_CHANNEL = getenv(
   " YAFA_CHANNEL", "https://t.me/darMahd313"
)


FAILED = "https://telegra.ph/file/f8995139e4f503955150b.jpg"
