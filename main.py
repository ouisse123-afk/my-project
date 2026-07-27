from telegram import Bot
from telegram.constants import ParseMode
import os
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="✅ بوت إشارات التداول يعمل بنجاح.",
        parse_mode=ParseMode.HTML
    )

if __name__ == "__main__":
    asyncio.run(main())
