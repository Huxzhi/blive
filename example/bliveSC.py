from blive import BLiver, Events, BLiverCtx
from blive.msg import SuperChatMsg
import requests
import time
# 转发弹幕

app = BLiver(22625027)  # 乃0
# app = BLiver(22637261)  # 嘉然
# app = BLiver(22632424)  # 贝拉
# app = BLiver(22384516)  # 呜米
# app = BLiver(21452505)  # 七海
# app = BLiver(22625025)  # 向晚

# 私人api，请换成自己的，项目成熟之后，我自己也会进行更换
webhook_url = 'https://discord.com/api/webhooks/xxxxxxxx'
print("start")


@app.on(Events.SUPER_CHAT_MESSAGE)
async def listen_sc(ctx: BLiverCtx):
    msg = SuperChatMsg(ctx.body)

    username = msg.sender['name'] + ' (uid: ' + str(msg.sender['id']) + ') 转发'
    # 颜色 需要 16 进制转 10 进制 字符串
    color = str(int(msg.color[1:], 16))
    start_time = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(msg.start_time))
    # 粉丝牌的主播名字
    anchor_uname = msg.anchor_uname
    price = '¥' + str(msg.price)
    title = msg.content if msg.content else "空白SC"
    data = {
        'username': username,
        'avatar_url': msg.avatar_url,
        'embeds': [{
            'title': title,
            'description': f"{price} \t发送给: {anchor_uname} \t发送时间: {start_time}",
            'color': color
        }]
    }
    print(f"{start_time}\t{anchor_uname}\t{username}:{price}\t{title}")
    try:
        # 转发利用 webhook 到discord
        r = requests.post(webhook_url, json=data, timeout=20)
        r.raise_for_status()
    except requests.exceptions as err:
        print(err.message)
# 启动
app.run()
