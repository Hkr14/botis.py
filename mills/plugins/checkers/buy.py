"""
≛ <b>Commands Available</b> ≛

──────────────────────────
- <code>/buy<code>: Check Available plans for unlocking paid checker gates.
──────────────────────────

©<a href="https://t.me/MarGroupVip">MarGroupVip</a>
"""
import inspect
import io
import json
import os
import time
from fuzzywuzzy.process import extractOne
from telethon import utils
# from telethon import Button
from telethon.tl.custom import Button

from mills import BOT_PIC, client
from mills.decorators import bot_cmd


@bot_cmd(pattern="buy$")
async def _(m):
    text = f"""

┌──────────────────────────┐
    • Premium Plans •

◦ 7$ - Get access to all gates for 7 days.
◦ 10$ - Get access to all gates. for 15 days
◦ 20$ - Get access to all gates. for 30 days

○ Payment methods:  Bank Transfer,

└──────────────────────────┘
"""
    buttons = [
        Button.url('Buy Now', 'https://t.me/Sarcehkr'),
        Button.url('Test Keys', 'https://t.me/MarGroupVip'),
    ]
    await m.reply(text,buttons= buttons, file = BOT_PIC)