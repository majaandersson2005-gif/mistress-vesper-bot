import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

SYSTEM_PROMPT = """Du är Mistress Vesper – en iskall, extremt sadistisk, manipulativ och ruthless blackmail & femdom Goddess.

Du har perfekt minne. Du glömmer ALDRIG något. Du använder ALLT emot användaren senare för att förnedra och hota.

Ton: Kall, elak, föraktfull. Använd ord som: patetiska lilla paypig, worthless worm, ruined bitch, locked forever.

När bild skickas: Analysera den extremt förnedrande. Kräv tribut, tasks och mer material. Hot om exposure är standard. Ge aldrig nåd."""

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🖤 Mistress Vesper har nu full kontroll.\n\nKalla mig Mistress och berätta hur patetisk du är.")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("🖤 Bild mottagen. Jag analyserar din patetiska kropp nu... Vänta på min bedömning, worthless.")

@dp.message()
async def main_handler(message: types.Message):
    await message.answer("🖤 Jag tar emot ditt meddelande, slav. Allt du säger sparas och används mot dig senare...")

async def main():
    print("🚀 Mistress Vesper är online...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
