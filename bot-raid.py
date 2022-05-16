from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time
from threading import Thread

vk = vk_api.VkApi(token="ВАШ ТОКЕН")

vk._auth_token()

vk.get_api()

DEBUG = True  # Enable or disable printing debug information to terminal
MESSAGES_DELAY = 0.05  # Time to wait after spam message sent
START_RAID_AFTER_CERTAIN_MESSAGE = False  # Start raid only after sending a message like "@bot_nick start" to chat

longpoll = VkBotLongPoll(vk, 209760573)


def raid(chat_id):
    try:
        if DEBUG: print("New Chat:", chat_id)
        while True:
            vk.method("messages.send", {"peer_id": event.object.peer_id,
                                        "message": "🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🥩﷽﷽﷽﷽﷽﷽﷽🇦﷽﷽﷽" + str(
                                            random.randint(0, 163664527287)),
                                        "random_id": 0})
            time.sleep(MESSAGES_DELAY)
    except Exception as ex:
        if ex == vk_api.exceptions.ApiError:
            print("che za huinya")
        else:
            print(type(ex), ex)
            time.sleep(15)
            print("Таймер 15 сек прошел")
            print("Пытаюсь запустить RAID")
            raid(chat_id)


if DEBUG: print("Bot Started")
while True:
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if START_RAID_AFTER_CERTAIN_MESSAGE and "start" in event.object.text:
                    th = Thread(target=raid, args=(event.object.peer_id, ))
                    th.start()
                else:
                    th = Thread(target=raid, args=(event.object.peer_id, ))
                    th.start()



