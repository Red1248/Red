import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, query):
        url = await self.search_youtube(query)
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            voice_client = await voice_channel.connect()
            voice_client.play(discord.FFmpegPCMAudio(url))
        else:
            await ctx.send("You need to be in a voice channel to use this command.")

    async def search_youtube(self, query):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'ytsearch:{query}', download=False)
            url = info['entries'][0]['url']
        return url

def setup(bot):
    bot.add_cog(Music(bot))
