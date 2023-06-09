from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

load_dotenv()


intents = discord.Intents.default()

bot = commands.Bot(intents=intents, command_prefix=commands.when_mentioned_or("!"))

watch_channel = str(getenv("CHANNEL_ID"))
role_id = int(getenv("ROLE_ID"))

@bot.event
async def on_message(message: discord.Message):
    # The docs say this isn't needed, but just in case
    if message.author == bot.user:
        return
    
    role = message.guild.get_role(role_id)

    if role in message.author.roles:
        return

    if str(message.channel.id) == watch_channel:
        return await message.author.add_roles(role)


bot.run(getenv("BOT_TOKEN"), log_handler=None)
