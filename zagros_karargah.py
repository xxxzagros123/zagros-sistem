import os
import discord
from discord.ext import commands

BOT_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} aktif ve baglandi!")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
