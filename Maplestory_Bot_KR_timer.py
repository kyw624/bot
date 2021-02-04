import os
import time
import discord
import asyncio
from datetime import datetime
# 플리 자동추가 테스트용
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
channels = [640176809752920065, 640875475291602974, 806430821903892540]

"""
@client.event
# 메이플 경뿌 알림
async def on_ready():

    while True:
        now = datetime.utcnow().minute
        if now == 29 or now == 59:  # 알림을 받을 시간 지정
            for i in range(len(channels)):
                await client.get_channel(channels[i]).send("경뿌 1분 전")  # 보낼 메시지 설정
            time.sleep(60)  # 60초 후 재탐색
        else:
            time.sleep(1)  # 1초 후 재탐색
"""

# 플리 자동추가 테스트용
playlist = ["-p https://www.youtube.com/watch?v=Md_I9quMmlE",
"-p https://www.youtube.com/watch?v=dB-0PAakOyw",
"-p https://www.youtube.com/watch?v=zp8FlinOyFo",
"-p https://www.youtube.com/watch?v=mAjLgh9Tw48",
"-p https://www.youtube.com/watch?v=_s84FLFVQM8",
"-p https://www.youtube.com/watch?v=XEsfzAgdzlM",
"-p https://www.youtube.com/watch?v=oeMA2RK-pQE",
"-p https://www.youtube.com/watch?v=aZCfbL5oIeI",
"-p https://www.youtube.com/watch?v=e0--itBVfa0",
"-p https://www.youtube.com/watch?v=1OsGRRcOUwY",
"-p https://www.youtube.com/watch?v=-EPXWXQUXDM",
"-p https://www.youtube.com/watch?v=UMWBdzQSr_I",
"-p https://www.youtube.com/watch?v=aepREwo5Lio",
"-p https://www.youtube.com/watch?v=h0o8EtwCDaQ",
"-p https://www.youtube.com/watch?v=Ou1xUChEDKM",
"-p https://www.youtube.com/watch?v=xR-M7mfph_I",
"-p https://www.youtube.com/watch?v=usc7DwVPTdk",
"-p https://www.youtube.com/watch?v=cvmxxXynwAQ",
"-p https://www.youtube.com/watch?v=sZ9GwLuvnuk",
"-p https://www.youtube.com/watch?v=J7c4mc6lkxI",
"-p https://www.youtube.com/watch?v=pSOxBAiN1lE",
"-p https://www.youtube.com/watch?v=X_SuQ_W_wJE",
"-p https://www.youtube.com/watch?v=5C-UzW1FLiA",
"-p https://www.youtube.com/watch?v=b8lfZ0AoEho",
"-p https://www.youtube.com/watch?v=o6QeCDp2oyU",
"-p https://www.youtube.com/watch?v=sPReSL8DxEg",
"-p https://www.youtube.com/watch?v=KWSpQeKPK9A",
"-p https://www.youtube.com/watch?v=kMt0muFdmYc",
"-p https://www.youtube.com/watch?v=jWkWa0rCuWU",
"-p https://www.youtube.com/watch?v=sPqa2NWSGig",
"-p https://www.youtube.com/watch?v=iHJcBb1iQ9A",
"-p https://www.youtube.com/watch?v=B8oG22CwMj4",
"-p https://www.youtube.com/watch?v=25-ScefZlW0",
"-p https://www.youtube.com/watch?v=6GFI2Bn8KQk",
"-p https://www.youtube.com/watch?v=j4td0_efDkc",
"-p https://www.youtube.com/watch?v=j_yvAB22S3c",
"-p https://www.youtube.com/watch?v=Af1Pi45RHAE",
"-p https://www.youtube.com/watch?v=opGokaA9xnc",
"-p https://www.youtube.com/watch?v=bsgBUM2Mnsw",
"-p https://www.youtube.com/watch?v=xJiGK8p-hIo",
"-p https://www.youtube.com/watch?v=HWnhaovaJws",
"-p https://www.youtube.com/watch?v=6GYD6q1d8rc",
"-p https://www.youtube.com/watch?v=_qP14y6kMHU",
"-p https://www.youtube.com/watch?v=JSuOMvgXnaM",
"-p https://www.youtube.com/watch?v=s6bx7MCEZ6Y",
"-p https://www.youtube.com/watch?v=ywwU5ka1fBs",
"-p https://www.youtube.com/watch?v=e_-U6M_Nq-U",
"-p https://www.youtube.com/watch?v=yNIWB4sjin0",
"-p https://www.youtube.com/watch?v=OOS7mvspJAA",
"-p https://www.youtube.com/watch?v=jBAdBd_hd-8",
"-p https://www.youtube.com/watch?v=JR-wv5fOJEY",
"-p https://www.youtube.com/watch?v=cQbHjOduepU",
"-p https://www.youtube.com/watch?v=gS8y9oYSFIQ",
"-p https://www.youtube.com/watch?v=UukrQJ--H30",
"-p https://www.youtube.com/watch?v=SIZbft9u-ac",
"-p https://www.youtube.com/watch?v=0D28qd--kRE",
"-p https://www.youtube.com/watch?v=zyqR7Ncnnp0",
"-p https://www.youtube.com/watch?v=xAQrGnCyFIU",
"-p https://www.youtube.com/watch?v=Q0sZX07H2Ew",
"-p https://www.youtube.com/watch?v=nzqgWX__KCU",
"-p https://www.youtube.com/watch?v=2kj-78NZRKk",
"-p https://www.youtube.com/watch?v=4qIy2869wLM",
"-p https://www.youtube.com/watch?v=c8VARXXU_VY",
"-p https://www.youtube.com/watch?v=l0Vp5u5nkFI",
"-p https://www.youtube.com/watch?v=p88Wl90xwM4",
"-p https://www.youtube.com/watch?v=hrH3rebaRig",
"-p https://www.youtube.com/watch?v=x7l0kLFN6Oc",
"-p https://www.youtube.com/watch?v=V3k5cK4LRaQ",
"-p https://www.youtube.com/watch?v=14JAzHVzAnk",
"-p https://www.youtube.com/watch?v=MevD7KtoaaM",
"-p https://www.youtube.com/watch?v=Yzb5lay6ykE",
"-p https://www.youtube.com/watch?v=LSgJSnrl53w",
"-p https://www.youtube.com/watch?v=8xt2mmCP_-s",
"-p https://www.youtube.com/watch?v=_NwNsJ0ufS8",
"-p https://www.youtube.com/watch?v=3hrHjHiEfuM",
"-p https://www.youtube.com/watch?v=GdNbfXqcOJ8",
"-p https://www.youtube.com/watch?v=t3ILnMBSl9I",
"-p https://www.youtube.com/watch?v=ZaNLd-HEwJA",
"-p https://www.youtube.com/watch?v=fLuYaG-Qvyo",
"-p https://www.youtube.com/watch?v=i7cSojnHbBw",
"-p https://www.youtube.com/watch?v=3DyP4aUTA24",
"-p https://www.youtube.com/watch?v=gJQNOXB2CP8",
"-p https://www.youtube.com/watch?v=mJj27PGA6SY",
"-p https://www.youtube.com/watch?v=j1r7i_3Ga60",
"-p https://www.youtube.com/watch?v=RfxSxk2YuaU",
"-p https://www.youtube.com/watch?v=kjYqlYWrrEI",
"-p https://www.youtube.com/watch?v=rJGUmo30zak",
"-p https://www.youtube.com/watch?v=vGYtZP_cSps",
"-p https://www.youtube.com/watch?v=XAz_jfS7mA4",
"-p https://www.youtube.com/watch?v=38a6tFduAHE",
"-p https://www.youtube.com/watch?v=rxl9cIbBHrc",
"-p https://www.youtube.com/watch?v=Rzg0AMltXzY",
"-p https://www.youtube.com/watch?v=dj1e5l70T0M",
"-p https://www.youtube.com/watch?v=P8N4nloV788",
"-p https://www.youtube.com/watch?v=ackPSn6UTi4",
"-p https://www.youtube.com/watch?v=i71ee1R8GYc",
"-p https://www.youtube.com/watch?v=S5r69y_OHiA"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("플리쿤"))


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("!test"):
        await message.channel.send("테스트 메시지")
    if message.content == "!loop":
        num = 1
        await message.channel.send('테스트 시작 >> ' + num)
        while (num < 10):
            await message.channel.send('테스트 메시지 >> ' + num)
            num += 1
        await message.channel.send('테스트 종료!! ' + num)


# async def on_message(message):
#     content = message.content
#     num = 1
#     if content == "!플리":
#         for music in playlist:
#             await message.channels[2].send(music)
#             time.sleep(2)
#     if content == '!test':
#         while (num < 10):
#             await message.channels[2].send('테스트 메시지 >> ' + num)
#             num += 1
#         print('테스트 종료!! ' + num)
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)  # 봇의 토큰 입력
