from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from googletrans import Translator

from linebot.models import *



app = Flask(__name__)

line_bot_api = LineBotApi('G0RKQaSPIfgz5nGrBfAH+2ofJ8MlIYmwFTNAMyRywRNBn4bhbYiQKtafWBxdc7F9OV6ECxZT8hobRcGoFDMDSZYMoCXNxyuQq7ZYIK8eRce0A0i5suwOw7Ai8W/SLlBMN33ne97Za1sM0YQEDrzOAAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3d8e1525dab2bc2dc7e41baacb2058f7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="hello world"))


if __name__ == "__main__":
    app.run()



