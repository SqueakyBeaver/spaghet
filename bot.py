from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

load_dotenv()


intents = discord.Intents.default()

bot = commands.Bot(intents=intents, command_prefix=commands.when_mentioned_or("!"))


@bot.event
async def on_message(message: discord.Message):
    print("in")
    print(message.author.id)
    print(str(message.channel.id) + "==?" + str(getenv("CHANNEL_ID")))
    # The docs say this isn't needed, but just in case
    if message.author == bot.user:
        return

    if str(message.channel.id) == str(getenv("CHANNEL_ID")):
        print("in2")
        await message.author.add_roles(message.guild.get_role(int(getenv("ROLE_ID"))))


bot.run(getenv("BOT_TOKEN"))
