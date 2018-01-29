import asyncio
import discord
import random
import math
from modules import *

client = discord.Client()

a=open('token.txt', 'r')
token = a.readline()
a.close()
token=token.strip()

@client.event
async def on_ready():
    print(client.user.name,'접속')
    await client.change_presence(game=discord.Game(name="!명령어", type=1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith('!랜덤'):
        random_num=random.randint(1,int(message.content[3:]))
        await client.send_message(channel, random_num)

    if message.content.startswith('!foseja'):
        random_num=random.randint(1,int(message.content[7:]))
        await client.send_message(channel, random_num)

    if message.content.startswith('!ㄱ무애ㅡ'):
        random_num=random.randint(1,int(message.content[5:]))
        await client.send_message(channel, random_num)

    if message.content.startswith('!random'):
        random_num=random.randint(1,int(message.content[7:]))
        await client.send_message(channel, random_num)

    elif message.content.startswith('ㅋ'):
        await client.send_message(channel, 'ㅋㅋㅋㅋㅋㅋㅋㅋ')

    elif message.content.startswith('z'):
        await client.send_message(channel, 'ㅋㅋㅋㅋㅋㅋㅋㅋ')

    elif message.content.startswith('!소인수분해'):
        MD=Microphage_decomposition(int(message.content[6:]))
        await client.send_message(channel, MD.calculate())

    elif message.content.startswith('!thdlstnqnsgo'):
        MD=Microphage_decomposition(int(message.content[13:]))
        await client.send_message(channel, MD.calculate())

    elif message.content.startswith('!약분'):
        value=message.content[3:]
        value=value.strip()
        value=value.split(' ')
        ROF=reduction_of_a_fraction(int(value[0]), int(value[1]))
        await client.send_message(channel, ROF.calculate())

    elif message.content.startswith('!dirqns'):
        value=message.content[7:]
        value=value.strip()
        value=value.split(' ')
        ROF=reduction_of_a_fraction(int(value[0]), int(value[1]))
        await client.send_message(channel, ROF.calculate())

    elif message.content.startswith('!명령어'):
            await client.send_message(channel, '!랜덤 수\n!소인수분해 수\n!약분 수1 수2\n!더하기(+)/빼기(-)/곱하기(*)/나누기(/) 수1 수2\n!연립방정식 ax+by=c ax\'+by\'=c\'\n!all\n!이차방정식 ax^2+bx+c=0\n!개발자\n!봇')

    elif message.content.startswith('!audfuddj'):
            await client.send_message(channel, '!랜덤 수\n!소인수분해 수\n!약분 수1 수2\n!더하기(+)/빼기(-)/곱하기(*)/나누기(/) 수1 수2\n!연립방정식 ax+by=c ax\'+by\'=c\'\n!all\n!이차방정식 ax^2+bx+c=0\n!개발자\n!봇')

    elif message.content.startswith('!더하기'):
        value=message.content[4:]
        value=value.split()
        await client.send_message(channel, int(value[0])+int(value[1]))

    elif message.content.startswith('+'):
        value=message.content[1:]
        value=value.split()
        await client.send_message(channel, int(value[0])+int(value[1]))

    elif message.content.startswith('!ejgkrl'):
        value=message.content[7:]
        value=value.split()
        await client.send_message(channel, int(value[0])+int(value[1]))

    elif message.content.startswith('-'):
        value=message.content[1:]
        value=value.split()
        await client.send_message(channel, int(value[0])+int(value[1]))

    elif message.content.startswith('!빼기'):
        value=message.content[3:]
        value=value.split()
        await client.send_message(channel, int(value[0])-int(value[1]))

    elif message.content.startswith('!Qorl'):
        value=message.content[5:]
        value=value.split()
        await client.send_message(channel, int(value[0])-int(value[1]))

    elif message.content.startswith('!곱하기'):
        value=message.content[4:]
        value=value.split()
        await client.send_message(channel, int(value[0])*int(value[1]))

    elif message.content.startswith('*'):
        value=message.content[1:]
        value=value.split()
        await client.send_message(channel, int(value[0])*int(value[1]))

    elif message.content.startswith('!rhqgkrl'):
        value=message.content[8:]
        value=value.split()
        await client.send_message(channel, int(value[0])*int(value[1]))

    elif message.content.startswith('!나누기'):
        value=message.content[4:]
        value=value.split()
        if value[1]=='0':
            await client.send_message(channel, '0으로 못나눔')
        else:
            await client.send_message(channel, int(value[0])/int(value[1]))

    elif message.content.startswith('/'):
        value=message.content[1:]
        value=value.split()
        if value[1]=='0':
            await client.send_message(channel, '0으로 못나눔')
        else:
            await client.send_message(channel, int(value[0])/int(value[1]))

    elif message.content.startswith('!sksnrl'):
        value=message.content[7:]
        value=value.split()
        if value[1]=='0':
            await client.send_message(channel, '0으로 못나눔')
        else:
            await client.send_message(channel, int(value[0])/int(value[1]))

    elif message.content.startswith('!연립방정식'):
        value=message.content[6:]
        value=value.strip()
        value=value.replace("x+", " ")
        value=value.replace("x'+", " ")
        value=value.replace("y=", " ")
        value=value.replace("y'=", " ")
        value=value.split()
        se=simultaneous_equations(int(value[0]), int(value[1]), int(value[2]), int(value[3]), int(value[4]), int(value[5]))
        await client.send_message(channel,se.calculate())

    elif message.content.startswith('!dusflqqkdwjdtlr'):
        value=message.content[15:]
        value=value.strip()
        value=value.replace("x+", " ")
        value=value.replace("x'+", " ")
        value=value.replace("y=", " ")
        value=value.replace("y'=", " ")
        value=value.split()
        se=simultaneous_equations(int(value[0]), int(value[1]), int(value[2]), int(value[3]), int(value[4]), int(value[5]))
        await client.send_message(channel,se.calculate())

    elif message.content.startswith('!이차방정식'):
        value=message.content[6:]
        value=value.strip()
        value=value.replace("x^2+", " ")
        value=value.replace("x=", " ")
        value=value.split()
        qe=a_quadratic_equation(int(value[0]),int(value[1]),int(value[2]))
        await client.send_message(channel,qe.calculate())

    elif message.content.startswith('!all'):
        value=message.content[4:]
        await client.send_message(channel, '@everyone'+' '+value)

    elif message.content.startswith('!미ㅣ'):
        value=message.content[4:]
        await client.send_message(channel, '@everyone'+' '+value)

    elif message.content.startswith('!개발자'):
        await client.send_message(channel, '이메일:neargul@naver.com/neargul@gmail.com\n블리자드:니얼굴#31112\n깃허브:https://github.com/Yorface/discord_bot')

    elif message.content.startswith('!봇'):
        output='%s %s'%(client.user.name,client.user.id)
        await client.send_message(channel, output)

client.run(token)
