import asyncio
from typing import Union
from datetime import datetime, timedelta
from AfkRobot import cleanmode, app, botname
from AfkRobot.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://telegra.ph/file/52e152c4f036384c84ae1.jpg",
    "https://telegra.ph/file/eb497a972df5836c1ebb9.jpg",
    "https://telegra.ph/file/3bf367b3ca7ccaadf339e.jpg",
    "https://telegra.ph/file/2b372cacca849f487039b.jpg",
    "https://telegra.ph/file/34d55f43d38e55ae001e9.jpg",
    "https://telegra.ph/file/8ff6b3dfbb3abb476c6d4.jpg",
    "https://telegra.ph/file/ec190771212ca366f2cbd.jpg",
    "https://telegra.ph/file/12549f809c7533e6c4197.jpg",
    "https://telegra.ph/file/a8cf5423ea950d28998c0.jpg",
    "https://telegra.ph/file/144551776656b05682d42.jpg",
    "https://telegra.ph/file/a2ea5c6d1099be896d79f.jpg", 
    "https://telegra.ph/file/661626d941bc44a97edf4.jpg"
]


HELP_TEXT = f"""ㅤ[ㅤㅤㅤㅤㅤ ](https://telegra.ph/file/661626d941bc44a97edf4.jpg)ㅤㅤ
■ Hᴇʏ Gᴜʏs, 

※ Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ᴏғ ᴀғᴋ ʙᴏᴛ

※ Tʜɪs ʙᴏᴛ ᴘʀᴏᴠɪᴅᴇs sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇ... 

☆ Tʜᴀᴛ ɪs ɪғ ʏᴏᴜ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴏ ɪғ ʏᴏᴜ ɢᴏɴᴇ ᴀғᴋ ᴀғᴛᴇʀ ᴛᴇʟʟɪɴɢ ᴛʜɪs ʙᴏᴛ ʙʏ ᴄᴏᴍᴍᴀɴᴅs 😉. 

☆ Oᴛʜᴇʀ ᴘᴇʀsᴏɴ ᴡʜᴏ ᴛᴀɢɢɪɴɢ ʏᴏᴜ ᴡɪʟʟ ᴀʙʟᴇ ᴛᴏ ᴋɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴏғғʟɪɴᴇ & ᴀғᴋ 😉.

● 𝐇𝐄𝐑𝐄 𝐈𝐒 𝐒𝐎𝐌𝐄 𝐔𝐒𝐄𝐅𝐔𝐋𝐋 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 🥶

◆ **𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴 𝘍𝘰𝘳 𝘈𝘍𝘒 :-** 

/afk - [ Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ɪɴ ʀᴇᴘʟʏ ᴏғ ᴀɴʏ Sᴛɪᴄᴋᴇʀ/Pʜᴏᴛᴏ/Gɪғ ]

 [ Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʏᴏᴜʀ ᴀғᴋ ʀᴇᴀsᴏɴ ᴡɪᴛʜ ʀᴇᴘʟʏ ᴏғ Sᴛɪᴄᴋᴇʀ/Gɪғ/Pʜᴏᴛᴏ ]

𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :- 

`/afk `

`/afk Going Offline For Study`

◆ **𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴 𝘍𝘰𝘳 𝘚𝘦𝘵𝘵𝘪𝘯𝘨𝘴 :- **

/settings - [ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴄʜᴀɴɢɪɴɢ sᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs ᴏғ Aғᴋ Bᴏᴛ ( Oɴʟʏ Usᴇ Iɴ Gʀᴏᴜᴘs) ]

🖇★ Rᴇɢᴀʀᴅs ~ [TʜᴇAFKʀᴏʙᴏᴛ](https://t.me/TheAfkRobot) 🔥. 
ㅤ
"""
            
def settings_markup(status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="↻ Cʟᴇᴀɴ Mᴏᴅᴇ ↺", callback_data="cleanmode_answer"),
            InlineKeyboardButton(
                text="✯ Eɴᴀʙʟᴇᴅ ✯" if status == True else "✕ Dɪsᴀʙʟᴇᴅ ✕",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ ᴍᴇɴᴜ", callback_data="close"),
        ],
    ]
    return buttons
