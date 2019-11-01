import requests


def post_facebook(img_path, token, object_id, text=''):
    '''
    get_token - https://developers.facebook.com/tools/explorer
    API - https://developers.facebook.com/docs/graph-api/photo-uploads/#single
    '''

    params = {
        'caption': text,
        'access_token': token
    }

    with open(img_path, 'rb') as image_file_descriptor:
        files = {'photo': image_file_descriptor}

        response = requests.post('https://graph.facebook.com/{}/photos'.format(object_id), files=files, params=params)
        response.raise_for_status()
