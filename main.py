# coding=utf-8
# python3 main.py
import json
import random
import websocket
from threading import Thread
from flask import Flask

# 配置bot信息
bot_name = 'SprinkleBot'
password = ' '
channel = 'your-channel'
hello = True
roll = True

app = Flask(__name__)
@app.route("/")
def main():
    return "alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target = run)
t.start()
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'
'''

bz = '''
### SprinkleBot 帮助
命令列表
| 表情包 | 趣站 | 涩图 | 手气 | 蛤 |  ﾟ∀ﾟ)σ |
'''
admin_bz = '''/w Sprinkle 
管理员命令列表
bot休眠
bot停止休眠
bothello
botroll
bot变色
bot出去
'''
# 加入和发送函数
def join(bot_name, password, channel):
    ws.send(json.dumps({'cmd': 'join', 'nick': bot_name, 'pass': password, 'channel': channel }))

def send(message):
    ws.send(json.dumps({'cmd': 'chat', 'text': message}))

# 功能列表
emprs_list = ['( ﾟ∀。)', '(ノﾟ∀ﾟ)ノ', ' ﾟ∀ﾟ)σ', '(*ﾟーﾟ)', '( ﾟ∀ﾟ)', 'σ`∀´) ﾟ∀ﾟ)σ', '(((　ﾟдﾟ)))']

site_list = [
    'http://adarkroom.doublespeakgames.com/?lang=zh_cn',
    'https://www.sekai.co/trust/',
    'https://openarena.live/',
    'https://bruno-simon.com/',
    'https://sombras.app/?a=ZZffyi&b=Z33dhc',
    'https://favicon-pong.glitch.me/',
    'https://liferestart.syaro.io/view/',
    'https://win11.blueedge.me/',
    'https://dinoswords.gg/',
    'https://saythemoney.github.io/',
    'http://asciicker.com/',
    'https://m3o.xyz/',
    'https://rpgplayground.com/',
    'https://2020game.io/',
    'https://emojia.glitch.me/',
    'http://voxar.io/',
    'v1.windows93.net',
    'https://www.pcjs.org/',
    'https://win95.ajf.me/win95.html',
    'www.lemonjing.com',
    'www.shadiao.app',
    'https://multiuser-sketchpad-colors.glitch.me/',
    'http://league-of-heroes.herokuapp.com/',
    'https://appetize.io',
    'https://cmd.to/',
    'http://cursors.io/',
    ]
color_list = ['#4EEE94', '#00BFFF', '#FFFF00', '#FF6A6A', '#fff', '#FF0000', '#FF1493', '#90EE90']
# 连接
ws = websocket.WebSocket()
ws.connect("wss://hack.chat/chat-ws")
join(bot_name, password, channel)
send('(｡･∀･)ﾉﾞ嗨')
# 循环判定
while 1 == 1:
    msg = str(ws.recv())
    print(msg)
    if 'onlineAdd' in msg and hello == True:
        if '"nick":"Sprinkle"' in msg and '"trip":"EoZ5HO"' in msg:
            send('$\color{red}主\color{orange}人\color{yellow}早\color{green}上\color{blue}好\color{purple}( ﾟ∀。)$')
        else:
            send('hey!')
    elif '@SprinkleBot' in msg:
        send('hi，我是SprinkleBot，输入"帮助"来查看帮助内容！')
    elif '帮助' in msg and bot_name not in msg:
        send(bz)
        send(admin_bz)
    elif '涩图' in msg and bot_name not in msg:
        send('涩图一张，注意身体( ﾟ∀ﾟ) ![waifu](https://pic.sprinkle.workers.dev)')
    elif '表情包' in msg and bot_name not in msg:
        emprs = random.choice(emprs_list)
        send(emprs)
    elif '趣站' in msg and bot_name not in msg:
        site = random.choice(site_list)
        send(site)
    elif '手气' in msg and bot_name not in msg and roll == True:
        r = random.randint(0,11)
        send('摇出了' + str(r) + '')
    elif '蛤' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif ' ﾟ∀ﾟ)σ' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif 'bot变色' in msg and '"trip":"EoZ5HO"' in msg:
        color = random.choice(color_list)
        send('/color ' + color + '')
        send('艹艹艹艹艹巴啦啦小魔仙，变身！艹艹艹艹艹')
    elif 'bothello' in msg and '"trip":"EoZ5HO"' in msg:
        if hello == True:
            send('$HELLO设为False')
            hello = False
        elif hello == False:
            send('$HELLO设为True')
            hello = True
    elif 'botroll' in msg and '"trip":"EoZ5HO"' in msg:
        if hello == True:
            send('$ROLL设为False')
            roll = False
        elif hello == False:
            send('$ROLL设为True')
            roll = True
    elif 'bot休眠' in msg and '"trip":"EoZ5HO"' in msg:
        send('晚安')
        while 1 == 1:
            msg1 = str(ws.recv())
            print(msg1)
            if 'bot停止休眠' in msg1 and '"trip":"EoZ5HO"' in msg1:
                send('睡醒咯')
                break
            elif '@SprinkleBot' in msg1:
                send('SprinkleBot在睡觉呢')
    elif 'bot出去' in msg and '"trip":"EoZ5HO"' in msg:
        ws.close()
        break
