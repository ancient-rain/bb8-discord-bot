import discord
from discord.ext import commands
from starwarsfacts import facts
from random import *
import requests
import asyncio
import aiohttp

AUTHOR = '!author'
YOUTUBE = '!youtube'
FACT = '!fact'
GOOGLE_API_KEY = 'AIzaSyB3EHfKC4ewDs9s2c6EG1itBsiCyvwXzV4'


class Message(object):
    def __init__(self, client, channel, command):
        self.client = client
        self.channel = channel
        self.command = command

    async def executeCommand():
        if self.command.startswith(AUTHOR):
            await self.client.send_message(channel, sendAuthor('ɲuĸu'))
        elif self.command.startswith(YOUTUBE):
            search = message.content[len(YOUTUBE) + 1:]
            video_url = await get_youtube_url(search)
            await self.client.send_message(channel, video_url)
        elif command.startswith(FACT):
            fact = getFact()
            await self.client.send_message(channel, sendFact(fact))

    async def getFact():
        fact = sample(facts, 1)
        return fact[0]

    async def sendFact(fact):
        return '```md\n' + fact + '\n-------------\n< BB8 Facts >\n```'

    async def sendAuthor(author):
        return '```ini\n[  ' + author + '  ]\n```'

    async def getYoutubeUrl(search):
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
