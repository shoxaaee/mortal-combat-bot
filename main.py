import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

characters_stats = {
    "Liu Kang": 23,
    "Leatherface": 35,
    "Kung Lao": 22,
    "Triborg": 21,
    "Jax Briggs": 28,
    "Sub-Zero": 34,
    "Scorpion": 30,
    "D'Vorah": 29,
    "Goro": 38,
    "Mileena": 24,
    "Reptile": 20,
    "Alien": 39,
    "Raiden": 36,
    "Sonya Blade": 25,
    "Tanya": 26,
    "Shinnok": 37,
    "Bo'Rai Cho": 34,
    "Kenshi": 32,
    "Takeda Takahashi": 29,
    "Ermac": 28,
    "Kotal Kahn": 37,
    "Kung Jin": 24,
    "Ferra/Tor": 30,
    "Cassie Cage": 26,
    "Tremor": 36,
    "Jason Voorhees": 40,
    "Xishnik": 33,
    "Johnny Cage": 22,
    "Erron Black": 31,
    "Quan Chi": 36
}

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        parts = message.text.split(',')
        if len(parts) != 3:
            await message.reply("📌 Format noto‘g‘ri!\n\nYozish tartibi:\n`Jangchi1, Jangchi2, sekund`\n\nMasalan:\n`Scorpion, Sub-Zero, 28`", parse_mode="Markdown")
            return

        f1, f2, time = parts
        f1 = f1.strip()
        f2 = f2.strip()
        time = int(time.strip())

        if f1 not in characters_stats or f2 not in characters_stats:
            await message.reply("❌ Jangchi nomi topilmadi. Iltimos, to‘g‘ri yozing.\n\n📛 Mavjud jangchilar ro‘yxatini so‘rashingiz mumkin.")
            return

        avg_time = (characters_stats[f1] + characters_stats[f2]) / 2
        result = "KO‘PROQ 🕒" if avg_time > time else "KAMROQ ⚡️"

        text = (
            f"🔥 *{f1}* vs *{f2}* 🔥\n\n"
            f"📊 Ularning o‘rtacha jang vaqti: *{avg_time:.1f} sekund*\n"
            f"⏱ Siz tanlagan vaqt: *{time} sekund*\n\n"
            f"💥 Jang ehtimol shu vaqtdan *{result}* davom etadi!"
        )

        await message.reply(text, parse_mode="Markdown")

    except Exception as e:
        await message.reply("🚫 Xatolik yuz berdi:\n" + str(e))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
