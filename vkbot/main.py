from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
# t=
vk_session = vk_api.VkApi(token=t)
session_api=vk_session.get_api()
longpoll=VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('sad')