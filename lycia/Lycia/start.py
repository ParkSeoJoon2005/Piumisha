from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Hello, I am ⚡Ａｓｈ⚡, An Intelligent ChatBot by @iAmLiKu1.If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("⚡Ａｓｈ⚡", switch_inline_query_current_chat="lycia "), InlineKeyboardButton("Master 👑", url = "https://t.me/iAmLiKu1")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
