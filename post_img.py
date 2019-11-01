from dotenv import dotenv_values

from social_media.facebook import post_facebook
from social_media.telegram import post_telegram
from social_media.vkontakte import post_vkontakte

if __name__ == '__main__':
    dotenv_dict = dotenv_values()

    # img_path = 'test.jpg'
    # text = 'test'
    #
    # post_facebook(img_path, dotenv_dict['facebook_token'], dotenv_dict['facebook_group_id'], text)
    # post_telegram(img_path, dotenv_dict['telegram_token'], dotenv_dict['telegram_chat_id'], text)
    # post_vkontakte(img_path, dotenv_dict['vkontakte_token'], dotenv_dict['vkontakte_group_id'], text)
