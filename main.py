from datetime import datetime

import vk_api, requests, getpass, os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

def vk_bot():

    file = open('logins.txt', 'r')
    token = file.readline().strip()
    groupid = file.readline().strip()
    session = requests.Session()
    vk_session = vk_api.VkApi(token=token)

    long_poll = VkBotLongPoll(vk_session, group_id=groupid)
    vk = vk_session.get_api()
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.message.text:

            message = ''
            last_name = ''
            if event.message.from_id > 0:
                user_get = vk.users.get(user_ids=(event.message.from_id))
                user_get = user_get[0]
                last_name = user_get['last_name']

            if last_name == 'Криулин' and event.chat_id != 3:
                 continue

            # if last_name == 'Жуков':
            #      message = 'Сергей, вы пидор!'
            #'[club168038789|@botv_pidor] топ'

            inputMessageText = event.message.text
            list = inputMessageText.split()
            lastword = list[-1].lower()
            try:
                intLastword = int(lastword)
                isInt = True
            except:
                isInt = False

            if inputMessageText == 'Кажется, пидор дня - [id13508986|Александр Криулин]':
                message = '[club168038789|@botv_pidor] сам ты пидор!'

            if lastword == 'нет':  # Если написали заданную фразу
                message = 'Пидора ответ!'
            elif lastword == 'да':
                message = 'Пидора слова!'
            elif lastword == '300' or lastword == 'триста' or lastword == 'з00' or lastword == 'зоо' or lastword == '3оо' or (isInt and intLastword % 1000 == 300):
                message = 'Отсоси у тракториста!'
            elif lastword == 'гвоздика':
                message = 'Не пизди-ка!'
            elif lastword == 'аргумент':
                message = 'Аргумент не нужен, пидор обнаружен!'
            elif lastword == 'согласен':
                message = 'Кто согласен, тот как пидор ужасен!'

            if message != '' and event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    message=message,
                    random_id=get_random_id()
                )

vk_bot()
