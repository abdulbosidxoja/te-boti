from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from models import sqlite

startRT : Router = Router()

@startRT.message(CommandStart())
async def start(msg: Message):
    try:
        sqlite.User.id = msg.from_user.id
        sqlite.User.name = msg.from_user.full_name
        sqlite.User.email = "None"
        await sqlite.create_user(user=sqlite.User)
    except:
        pass

    await msg.answer(f"Assalom alaykum {msg.from_user.username} Xush kelibsiz!")    