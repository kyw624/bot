#!/usr/bin/env python3

import os
import time
import discord
from datetime import datetime

client = discord.Client()
channels = [640176809752920065, 640875475291602974]

@client.event
async def on_ready():
    while True:
        now = datetime.utcnow().minute
        if now == 55 or now == 56:  # 알림을 받을 시간 지정
            await client.get_channel(for i in channels: i).send("테스트")  # 보낼 메시지 설정
            time.sleep(60)  # 60초 후 재탐색
        else:
            time.sleep(1)  # 1초 후 재탐색
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)  # 봇의 토큰 입력
