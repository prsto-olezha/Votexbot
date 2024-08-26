from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, F
from config.token import TOKEN
from aiogram.enums import ParseMode

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


