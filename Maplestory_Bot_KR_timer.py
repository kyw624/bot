#!/usr/bin/env python3

import os
import time
import discord
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='', type=1))
    
@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await client.send_message(message.channel, "HI")

'''
@client.event
async def on_ready():
    while True:
        now = datetime.utcnow().minute
        if now == 29 or now == 59:  # 알림을 받을 시간 지정
            await client.get_channel(640176809752920065).send("경뿌 1분 전")  # 보낼 메시지 설정
            time.sleep(60)  # 60초 후 재탐색
        else:
            time.sleep(1)  # 1초 후 재탐색
'''
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)  # 봇의 토큰 입력
