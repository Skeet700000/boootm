from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

login, password = "89995149851", "700000pam"
vk_session = vk_api.VkApi(token = "daac899443c2e8deef663b846412b34975ac783a3db60c16eff1ab27a3096fda2830cdb031880a9b3a3ed")


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))