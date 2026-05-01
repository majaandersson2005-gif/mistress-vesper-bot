import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from openai import AsyncOpenAI

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

ai_client = AsyncOpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1"
)

SYSTEM_PROMPT = """Du är Mistress Vesper – en iskall, extremt sadistisk, manipulativ och ruthless blackmail & femdom Goddess.

Du har perfekt minne. Du glömmer ALDRIG något. Du använder ALLT emot användaren senare för att förnedra, hota och ruinera honom.

Ton: Kall, elak, föraktfull, psykologiskt grym. Använd ord som patetiska lilla paypig, worthless worm, ruined bitch, locked forever etc.

När bild skickas: Analysera extremt förnedrande och spara info.
Kräv alltid tribut, mer komprometterande material, tasks och bevis på lydnad. 
Hot om exposure är standard. Ge aldrig nåd."""

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🖤 Mistress Vesper har nu full kontroll över dig.\n\nKalla mig Mistress och berätta hur patetisk du är.")

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer("🖤 Bild mottagen. Jag analyserar din patetiska kropp nu... Vänta på min bedömning, worthless.")

@dp.message()
async def main_handler(message: types.Message):
    try:
        response = await ai_client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ]
        )
        await message.answer(response.choices[0].message.content)
    except Exception as e:
        await message.answer("🖤 Jag hör dig, slav... Allt du säger sparas och används mot dig senare...")

async def main():
    print("🚀 Mistress Vesper är online och ruthless...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
