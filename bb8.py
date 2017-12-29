import discord
from discord.ext import commands
from random import *
import requests
import asyncio
import aiohttp
from starwarsfacts import facts

CLIENT = discord.Client()
AUTHOR = '!author'
YOUTUBE = '!youtube'
SWFACT = '!fact'
GOOGLE_API_KEY = 'AIzaSyB3EHfKC4ewDs9s2c6EG1itBsiCyvwXzV4'

@CLIENT.event
async def on_ready():
    print('Logged in as')
    print(CLIENT.user.name)
    print(CLIENT.user.id)
    print('-------')

@CLIENT.event
async def on_message(message):
    command = message.content
    channel = message.channel

    if command.startswith(AUTHOR):
        await CLIENT.send_message(channel, sendAuthor())
    elif command.startswith(YOUTUBE):
        search = message.content[len(YOUTUBE) + 1:]
        video_url = await get_youtube_url(search)
        await CLIENT.send_message(channel, video_url)
    elif command.startswith(SWFACT):
        fact = getFact()
        await CLIENT.send_message(channel, sendFact(fact))

def getFact():
    fact = sample(facts, 1)
    return fact[0]

def sendFact(fact):
    return '```md\n' + fact + '\n-------------\n< BB8 Facts >\n```'

def sendAuthor():
    return '```ini\n[  ɲuĸu  ]\n```'


async def get_youtube_url(search):
    url = 'https://www.googleapis.com/youtube/v3/search'
    with aiohttp.ClientSession() as session:
        async with session.get(url, params={"type": "video",
                                            "q": search,
                                            "part": "snippet",
                                            "key": GOOGLE_API_KEY}) as resp:

            data = await resp.json()

    if not data.get("items"):
        raise Exception('An error occured searching for video')

    items = data["items"]
    if len(items) == 0:
        return None

    return 'https://youtube.com/watch?v=' + items[0]["id"]["videoId"]


CLIENT.run('Mzk0NjA1NjY1NzY0NTA3NjQ5.DSJGmg.P5pDRuHVmxbcK3FO2qhjxjJw9Xk')
