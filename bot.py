import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load extensions
initial_extensions = ['cogs.music']
for extension in initial_extensions:
    bot.load_extension(extension)

bot.run('TOKEN')
