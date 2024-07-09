import discord
from discord.ext import commands
import subprocess
import re

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def ping(ctx, *args):
    if args:
        await ctx.send("```\noopsie thats not the right command\n```", delete_after=5)
        return

    try:
        result = subprocess.run(['ping', 'google.com', '-n', '1'], capture_output=True, text=True)
        output = result.stdout
        match = re.search(r'Time[=<]\s*(\d+ms)', output, re.IGNORECASE)
        if match:
            ping_time = match.group(1)
        else:
            raise ValueError("Ping time not found in output")

    except Exception as e:
        await ctx.send(f"\n```Error : {str(e)}```\n", delete_after=5)
        return

    embed = discord.Embed(
        title="Ping Result",
        description=f"**Your ping <@{ctx.author.id}> :** `{ping_time}`",
        color=0xffffff
    )
    await ctx.send(embed=embed)

client.run('YOUR_TOKEN')
