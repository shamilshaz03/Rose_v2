import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = True
PICS = (environ.get('PICS' ,'https://graph.org/file/57dce571d4407480b911a.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/7d7cbf0d6c39dc5a05f5a.jpg")
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [1788725479, 557604719]
CHANNELS = [-1001776523617]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001635310944')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://1:1@cluster0.kf2htgv.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "1"
COLLECTION_NAME = 'Telegram_files'

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(6)
START_MESSAGE = environ.get('START_MESSAGE', '‎‎‎')
BUTTON_LOCK_TEXT = "⚠️ I am the സോറി അളിയാ❗ Ask your self"
FORCE_SUB_TEXT = "𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!"
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = ""
PMFILTER = False
G_FILTER = True
BUTTON_LOCK = True

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(-1001569522112)
SUPPORT_CHAT = 'ML_LINKS_01'
P_TTI_SHOW_OFF = True 
IMDB = False 
SINGLE_BUTTON = True
CUSTOM_FILE_CAPTION = """<b>➤ Fɪʟᴇ ɴᴀᴍᴇ 📂 :</b><b>{file_name}</b> <b>\n➤ Sɪᴢᴇ 👀 :</b><b>{file_size}</b> <b>\n╭─────── • ◆ • ───────╮ \n📮ᴊᴏɪɴ : <a href=https://t.me/ML_LINKS_01>ᴄʜᴀɴɴᴇʟ</a> \n❤️ Cᴇᴏ : <a href=https://t.me/CEO_shazbots \n╰─────── • ◆ • ───────╯   \n♡ ㅤ   ❍ㅤ     ⎙      ⌲   \nˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ   ˢᵃᵛᵉ   ˢʰᵃʳᵉ</b>"""
BATCH_FILE_CAPTION = None
IMDB_TEMPLATE = "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10"
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = "8"
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = None
MELCOW_NEW_USERS = False
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True

#log srt
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

