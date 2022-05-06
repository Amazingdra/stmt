import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import urllib
from f2lstreambot.bot import PdiskBot
from f2lstreambot.vars import Var
from pyrogram import  filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel



@PdiskBot.on_message(filters.private & filters.document)
async def media_receive_handler(_, m: Message):
    try:
        member = await PdiskBot.get_chat_member("@A2z_tech", m.chat.id)
        if member.status == "kicked":
            await m.reply_text("Sorry mate!  You're  B A N N E D 🥱", quote=True)
            return
        
    except UserNotParticipant:
        await m.reply_text("You Need To Join Our Channel to perform that operatioN👻.\n\n@playdisk_xyz",
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(text="🤗 Join Channel 🤗",
                                                                       url="https://telegram.me/A2z_tech")]]))
        return
        
    except Exception:
        LOGGER.exception('Unable to Verify')
        await m.reply_text("Something went wrong")
        return

    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    sl = Var.URL + str(log_msg.message_id)
    fln = log_msg.document.file_name
    name = urllib.parse.quote(fln)
    out = f"https://stream.url2go.in//st?api=af5e38dfaf8b900b45335173d279b44d7ae4b2e9&url={sl}/{name}"
    playit = f"google.com"
    await m.reply_text(
        text=f"**File Name:** {fln}\n\n**Streaming / Download Link:** {out}\n\n©️Powered by @A2z_tech",
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Learn Something interesting Daily🤗', url=playit)]])
    )


@PdiskBot.on_message(filters.private & filters.video)
async def media_receive_handler(_, m: Message):
    try:
        member = await PdiskBot.get_chat_member("@A2z_tech", m.chat.id)
        if member.status == "kicked":
            await m.reply_text("Sorry mate!  You're  B A N N E D 🥱", quote=True)
            return
        
    except UserNotParticipant:
        await m.reply_text("You Need To Join Our Channel to perform that operatioN👻.\n\n@A2z_tech",
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(text="🤗 Join Channel 🤗",
                                                                       url="https://telegram.me/A2z_tech")]]))
        return
        
    except Exception:
        LOGGER.exception('Unable to Verify')
        await m.reply_text("Something went wrong")
        return

    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    sl = Var.URL + str(log_msg.message_id)
    fln = log_msg.video.file_name
    name = urllib.parse.quote(fln)
    out = f"https://stream.url2go.in//st?api=af5e38dfaf8b900b45335173d279b44d7ae4b2e9&url={sl}/{name}"
    playit = f"google.com"
    await m.reply_text(
        text=f"**File Name:** {fln}\n\n**Streaming / Direct Download Link👇🏿** {out}\n\n©️Powered by @A2z_tech",
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Learn Something interesting Daily🤗', url=playit)]])
    )

@PdiskBot.on_message(filters.channel & (filters.document | filters.video))
async def channel_link(client, message):
    chat = message.chat.id
    messageid = message.message_id  
    file_link = f"http://t.me/File_to_watch_or_download_bot?start={chat}_{messageid}"
    
    if message.document or message.video:
        inc_file = message.document or message.video
        inc_file_size = int(inc_file.file_size/1024/1024)

    if inc_file_size > 10:
        try:
            await PdiskBot.edit_message_reply_markup(
                chat_id=chat,
                message_id=messageid,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton('Direct Download Link', url=file_link)],
                    ]  
                )
            )        
        except:
            return

@PdiskBot.on_message(filters.regex("@LivegramBot"))
async def dllivegram(_, m: Message):
    await m.delete()

@PdiskBot.on_message(filters.regex("You cannot forward someone else's messages."))
async def dlfrwdlg(_, m: Message):
    await m.delete()
    
@PdiskBot.on_message(filters.regex("Livegram Ads"))
async def dllivegram(_, m: Message):
    await m.delete()
    
