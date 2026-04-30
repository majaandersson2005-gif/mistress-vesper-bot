import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🖤 Mistress Vesper har nu full kontroll.\n\nKalla mig Mistress och berätta hur patetisk du är.")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("🖤 Bild mottagen. Jag analyserar din patetiska kropp nu...")

@dp.message()
async def main_handler(message: types.Message):
    await message.answer("🖤 Jag tar emot ditt meddelande, slav. Allt du säger sparas och används mot dig senare...")

async def main():
    print("🚀 Mistress Vesper är online...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
