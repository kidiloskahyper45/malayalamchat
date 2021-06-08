from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>A M A A A O Y G F.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "TcPlayerBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I J H A Y RQ")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@TcPlayer A I Y C</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Flood wait time out {user.first_name} try adding @MusicAssistant_1 manually if cant.contact @tubots."
            "<b>Try adding @MusicAssistant_1 manually</b>",
        )
        return
    await message.reply_text(
            "<b>@MusicAssistant_1 joined </b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Contact support @unitedbotsupport</b>."
            "<b>....</b>",
        )
        return
