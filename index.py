from config import *
from time import sleep
from telethon import TelegramClient, sync, events

client = TelegramClient('ghoul-session', api_id, api_hash)
client.start()
print('Ты - гуль')

my_id = client.get_me().id

@client.on(events.NewMessage())
async def normal_handler(event):

    if(hasattr(event.message.peer_id, 'user_id') and hasattr(event.message.from_id, 'user_id') and event.message.from_id.user_id == my_id and event.message.text == start_command):
        await client.get_dialogs()
        i = 1000
        while i > 0:
            sleep(1/messages_per_second)
            await client.send_message(event.message.peer_id.user_id, str(i)+' - 7 = '+str(i-7))
            i -= 7
        if(end_message != ''):
            await client.send_message(event.message.peer_id.user_id, end_message)

client.run_until_disconnected()
