import telegram


def post_telegram(img_path, token, chat_id, text=''):
    '''https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets'''

    bot = telegram.Bot(token=token)

    with open(img_path, 'rb') as image_file_descriptor:
        bot.send_photo(chat_id=chat_id, photo=image_file_descriptor, caption=text)
