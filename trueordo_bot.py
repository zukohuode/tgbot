from imaplib import Commands

import aiogram 
from aiogram import Bot, Dispatcher, types
from aiogram.types import message
from aiogram.types import (
    CallbackQuery,  # Добавили для обработки нажатий
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher()
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="❓ Правда", callback_data="truth"
            ),  # Кнопка Правда
            InlineKeyboardButton(
                text="⚡ Действие", callback_data="dare"
            ),  # Кнопка Действие
        ]
    ]
)

@dp.message(Commands("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hello, welcome to my bot!", reply_markup=keyboard)

@dp.callback_query(F.data == "truth")
async def command_truth(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Ты выбрал правду!")