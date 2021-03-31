import os
import secret
from notion.client import NotionClient

"""
TODO
Bot de proposito unico para entender as relações de dia/hora/local e pessoas
API Google
"""

cliente  = NotionClient(token_v2=os.getenv('TOKEN_V2'))

page = cliente.get_block('https://www.notion.so/Auto-test-877853b13a904fbab8a44476c46aa0bc')


for child in page.children:
    child = child.title
    if child[0] == '!':
        print(child)
        print('Call Google api agenda!!!')
    else:
        pass

