from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "4sᴛ 𝐎ғғɪᴄɪᴀʟ"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/f5b0e7f2bd95153968e87.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else"𝐆ᴇᴛ 𝐑ᴇᴀᴅʏ 𝐓ᴏ 𝐅ᴜᴄᴋ 𝐁ʏ #_4sᴛ"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
      **[👻4sᴛ 𝐎ғғɪᴄɪᴀʟ💘](https://t.me/I_M_FIGHTER)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 

➪ **👑4sᴛ 𝐅ʏᴛᴇʀ💌:** [𝐓ᴇʀᴀ 𝐁ᴀᴀᴘ #_4sᴛ](https://t.me/ll4st_MIND_GAMERII)

➪ **❤𝐏ʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ👀:**`{platform.python_version()}`

➪ **💞𝐓ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:💢** `{__version__}`

➪ **💌𝐏ʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ💤:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser