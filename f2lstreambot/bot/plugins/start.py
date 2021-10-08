
from f2lstreambot.bot import PdiskBot
from f2lstreambot.vars import Var
from pyrogram import filters, emoji
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@PdiskBot.on_message(filters.command(['help']))
async def start(b, m):
    await m.reply(f"""Hello {m.from_user.first_name},
    
I'm A simple link Generator Bot !💯.

Send me any TELEGRAM file, I'll generate instant stream/download link for you!

NB: You Need To Join Our Channel to Use This BoT..

©️Powered By @A2z_tech""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://telegram.me/A2z_tech")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/joinchat/nydQ9TrIeX01N2M1"),
                                                    InlineKeyboardButton(text="SHARE ♐️", url="https://t.me/share/url?url=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%0A%0A__Today%20i%20just%20found%20out%20an%20intresting%20and%20powerful__%20%2A%2AStreaming/Downloadable%20Link%20Generator%20Bot%2A%2A%20__for%20free%F0%9F%A5%B0.%20%0ACheck%20out%20%F0%9F%98%8B..__%0A%0A%2A%2ABot%20link%20%3A%20%40file_to_watch_or_download_bot%20%F0%9F%94%A5%2A%2A%0A%0A%60%C2%A9Powered%20by%60%20%40@A2z_tech")]])
        )

@PdiskBot.on_message(filters.command(["start"]))
async def start(client, message):

    if len(message.command) > 1:
        chatid, msgid = message.command[1].split("_")
       
        startlink = f"http://t.me/File_to_watch_or_download_bot?start={chatid}_{msgid}"
        try:
            await PdiskBot.get_chat_member("@A2z_tech", message.chat.id)
                
        except UserNotParticipant:
            await message.reply_text("You Need To Join Our Channel to perform that operatioN👻.\n\n@A2z_tech",
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(text="🤗 Join Channel 🤗",
                                                                       url="https://telegram.me/A2z_tech")],
                                         [InlineKeyboardButton(text="Generate Link",
                                                                           url=startlink)]]))
        return
       
        try:
            fd_msg = await PdiskBot.forward_messages(
                chat_id=Var.BIN_CHANNEL,
                from_chat_id=int(chatid),
                message_ids=int(msgid)
            )
        except:
            LOGGER.info("Channel start - Couldn't Forward messages")
            return
            
        media = fd_msg.document or fd_msg.video
        
        sl = Var.URL + str(fd_msg.message_id)
        out = f"https://link.playdisk.xyz/st?api=1cb40bcf2199038e39da5fe338a1f00f71c0911c&url={sl}"
        #if fd_msg.document:
            #fln = fd_msg.document.file_name
       # if fd_msg.video:
           # fln = fd_msg.video.file_name
        try:
            await message.reply_text(
                text=f"**File Name:** ``\n\n**Streaming Link:** {out}\n\n`©️Powered by` @A2z_tech",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton('Stream/download Now🤗', url=out)]
                    ]
                ),
                quote=True
            )
        except:
            return
    
    else:
        await message.reply(f"""Hello {message.from_user.first_name},

I'm A simple link Generator Bot !💯.

Send me any TELEGRAM file, I'll generate instant stream/download link for you!

NB: You Need To Join Our Channel to Use This BoT..

©️Powered By @playdisk_xyz""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://telegram.me/A2z_tech")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/joinchat/nydQ9TrIeX01N2M1"),
                                                    InlineKeyboardButton(text="SHARE ♐️", url="https://t.me/share/url?url=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%0A%0A__Today%20i%20just%20found%20out%20an%20intresting%20and%20powerful__%20%2A%2AStreaming/Downloadable%20Link%20Generator%20Bot%2A%2A%20__for%20free%F0%9F%A5%B0.%20%0ACheck%20out%20%F0%9F%98%8B..__%0A%0A%2A%2ABot%20link%20%3A%20%40file_to_watch_or_download_bot%20%F0%9F%94%A5%2A%2A%0A%0A%60%C2%A9Powered%20by%60%20%40playdisk_xyz")]])
        )
