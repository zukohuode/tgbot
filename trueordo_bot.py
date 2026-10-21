import aiogram 
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    CallbackQuery,  # Добавили для обработки нажатий
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram import F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

truth_questions = [
    "Какое самое неловкое сообщение ты отправлял не тому человеку?",
    "Чего ты больше всего боишься из того, чего другие не боятся?",
    "Какая твоя самая странная привычка?",
]

dare_actions = [
    "Сделай 10 приседаний и отправь голосовое с тяжелым дыханием.",
    "Напиши бывшему/бывшей «Привет, я нашел твою пропавшую вещь».",
    "Изобрази звуки умирающего кита в голосовом сообщении.",
]

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


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hello, welcome to my bot!", reply_markup=keyboard)

@dp.callback_query(F.data == "truth")
async def command_truth(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Ты выбрал правду!")
    question = random.choice(truth_questions)
    await callback_query.message.answer(
      f"❓ Правда:\n{question}", reply_markup=keyboard
    )

@dp.callback_query(F.data == "dare")
async def command_dare(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Ты выбрал действие!")
    action = random.choice(dare_actions)
    await callback_query.message.answer(
      f"⚡ Действие:\n{action}", reply_markup=keyboard
    )
