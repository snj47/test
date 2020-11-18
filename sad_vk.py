import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "1ec38452a02619f11c71e383337fb84e70dae8a3a7ce939b77fc0232dd35a29087263938fbb9caca5dcde"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            print(text)
                if text == "привет":
                  send_message(user_id, "ку")
                  print(text)

