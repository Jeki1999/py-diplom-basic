import requests
from pprint import pprint

with open('vk_token_file.txt') as vk_token_file:
    vk_token = vk_token_file.read()


URL = 'https://api.vk.com/method/photos.get'
params = {
    'owner_id': '182056708',
    'album_id': 'profile',
    'access_token': vk_token,
    'rev':'0',
    'extenden':'1',
    'v':'5.131'
}

res = requests.get(URL, params=params)
pprint(res.json())





# class VK:

#     def __init__(self, access_token, user_id, version='5.131'):
#            pass