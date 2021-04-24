import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import vk
from io import BytesIO
import requests
my_club_id = 203809544


my_prev_message = dict()
dict_numbers_memes = {'постирония': 0, 'школа': 1, 'программирование': 2}
id_to_name = {399014949: 'одмен', 327325126: 'Артур', 384574779: 'Андрей'}
#399014949
list_friends_cat_1 = [384574779, 327325126]
list_friends_cat_2 = [327325126]
dict_lonely_messages = {'гг*good*game*gg': ['вп', 'wp', 'well played'],
                        'которые я вложил в капитал*в капитал прожиточного': ['ты куда звонишь?'],
                        'которые я вложил': ['куда вложил?'],
                        }
input_zdraste = ['привет', 'здрасте', 'здрасьте', 'здравствуй', 'хай', 'прив', 'хеллоу', 'hello', 'здарова', 'вечер в хату', 'здарово', 'здрасте', 'дарова', 'доброе утор', 'добрый день', 'добрый вечер']
my_dela = ['как обычно', 'нормально', 'критически стабильно', 'отлично', 'у ведьмаков дела так, как они сами хотят',
               'балдёжно', 'суперски', 'хорошо']
my_creator = ['Как истинный Ведьмак, я был вопроспитан в Каэр Морхене. Своей настоящей Родины я не помню.',
              'Своим создателем я считаю Дмитрия из России. Крёстным отцом мне приходится Артур',
              'Моя жизнь - путешествие по просторам сети. Наверное, меня создал тот, кто создал эту сеть.']
nepon_words = ['Не понял, что вы сказали', 'Неизвестная команда',
               'Я не понял, повторите, пожалуйста, так, чтобы мне стало понятно', 'Не понял', 'Вы говорите на непонятном мне диалекте, повторите, я постараюсь понять', 'Не очень понял, что вы имеете в виду']
laughing_smiles = ['&#128518;', '&#128516;', '&#128514;']


def reply_message(vk_session, event):
    vk = vk_session.get_api()
    message_to_send = generate_message(event.obj.message['text'], event.obj.message['from_id'], vk_session)
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=message_to_send,
                     random_id=random.randint(0, 2 ** 64))


def reply_comment(vk_session, event):
    vk = vk_session.get_api()
    comment_to_send = generate_comment(event.obj.comment['text'], event.obj.comment['from_id'], vk_session)
    vk.messages.send(user_id=event.obj.comment['from_id'],
                     message=comment_to_send,
                     random_id=random.randint(0, 2 ** 64))


def send_a_picture(vk_session, id, picture):
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_messages([picture])
    print(photo)
    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
    print(vk_photo_id)
    vk = vk_session.get_api()
    vk.messages.send(user_id=id, attachment=[vk_photo_id], random_id=random.randint(0, 2 ** 64))


def if_l_elem_in_text(l, text):
    for elem in l:
        if elem in text:
            return True
    return False

def generate_message(text, id, vk_session):
    def send_a_meme(text, id, vk_session):
        unnamed_meme_cat = False
        global priority, dict_numbers_memes, input_zdraste, my_dela, my_creator
        if 'постирон' in text:
            pass
        elif 'черн' in text and 'юмор' in text:
            pass
        elif 'школ' in text:
            print(text)
            name_of_picture = f"G:\ДИМА\ВКонтакте\ВК бот\Мемы\Школа\sch{random.randint(1, dict_numbers_memes['школа'])}.jpg"
        elif 'интелл' in text or 'добр' in text:
            pass
        elif 'программирование' in text:
            print(text)
            name_of_picture = f"G:\ДИМА\ВКонтакте\ВК бот\Мемы\Программирование\prog{random.randint(1, dict_numbers_memes['программирование'])}.jpg"
        elif 'гачи' in text or 'gachi' in text or 'dunge' in text or 'cum' in text or 'slave' in text or 'muchi' in text:
            pass
        else:
            name_of_picture = f"G:\ДИМА\ВКонтакте\ВК бот\Мемы\Школа\sch{random.randint(1, dict_numbers_memes['школа'])}.jpg"
            unnamed_meme_cat = True
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages([name_of_picture])
        print(photo)
        vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
        print(vk_photo_id)
        vk = vk_session.get_api()
        vk.messages.send(user_id=id, attachment=[vk_photo_id], random_id=random.randint(0, 2 ** 64))

    if id in list_friends_cat_1:
        priority = 1
        my_zdraste = [f'Приветствую тебя, {id_to_name[id]}', f'Привет, {id_to_name[id]}', 'ооооо\nкакие люди\nпривет', 'привет', 'ку', 'хай', 'прив', 'хеллоу', 'здарова', 'вечер в хату', 'ооооо\nпривет', 'ооо\nпривет']
        my_dela.extend(['норм', 'всё зашибись', 'афигенно', 'балдёжно, почти как у человека'])
    elif id in list_friends_cat_2:
        my_zdraste = ["Gwynbleidd приветствует тебя, D'hoine. Как же приятно разговаривать с посвященным.",
                      f'Приветствую тебя, {id_to_name[id]}',
                      f'Приветствую тебя, {id_to_name[id]}. Благодаря Предназначению, мы наконец-то встретились.',
                      'Приветствую тебя, носитель Hen Ichaer']
        my_dela.extend(['норм', 'всё зашибись', 'афигенно', 'балдёжно, почти как у человека'])
    else:
        my_zdraste = ["Приветствую тебя, D'hoine. Как же давно я не использовал язык старшего народа...",
                      'Здравствуйте!', 'Вас приветствует Геральт из Ривии', 'Доброго времени суток']
    for zdraste in input_zdraste:
        if zdraste in text.lower():
            message_to_send = my_zdraste[random.randint(0, len(my_zdraste) - 1)]
            my_prev_message[id] = message_to_send
            return message_to_send
    if text.lower() == 'ку':
        message_to_send = my_zdraste[random.randint(0, len(my_zdraste) - 1)]
        my_prev_message[id] = message_to_send
        return message_to_send
    for send_word_input in ['кинь', 'брось', 'пришли', 'сообщи', 'напиши', 'распечатай', 'напечатай']:
        if send_word_input in text.lower():
            if 'мем' in text.lower() or 'прикол' in text.lower() or 'прекол' in text.lower() or 'пикч' in text.lower():
                send_a_meme(text.lower(), id, vk_session)
                return 'вот'
            elif 'адрес' in text.lower() or 'координаты' in text.lower():
                list_text = text.lower().split()
                for ind_of_word in range(1, len(list_text) + 1):
                    if list_text[(-1) * ind_of_word] in ['карте', 'адрес', 'координаты']:
                        address = list_text[(-1) * ind_of_word:]
                if address and ('на карте' in text.lower()) and 'организац' in text.lower():
                    try:
                        send_a_picture(vk_session, id, org_address_on_map(address))
                    except:
                        return 'не удалось выполнить запрос'
                    return 'вот'
                elif address and 'на карте' in text.lower():
                    try:
                        send_a_picture(vk_session, id, address_on_map(address))
                    except:
                        return 'не удалось выполнить запрос'
                    return 'вот'
                try:
                    resp = full_address_geo(address)
                    return resp
                except:
                    return 'не удалось выполнить запрос'
    for quest in ['как', 'зачем', 'почему', 'где', 'куда', 'откуда', 'когда', 'кто']:
        if quest in text.lower():
            if (('как' in text.lower()) and ('дела' in text.lower() or 'жизнь' in text.lower())) or text.lower() in ['как ты', 'как ты?', 'кд']:
                message_to_send = my_dela[random.randint(0, len(my_dela) - 1)]
                my_prev_message[id] = message_to_send
                return message_to_send
            elif 'как' in text.lower() and 'с деньгами' in text.lower():
                message_to_send = 'С какими деньгами'
                my_prev_message[id] = message_to_send
                return message_to_send
            elif 'кто' in text.lower() and ('твой' in text.lower() or 'тебя' in text.lower()):
                for maker_word in ['создатель', 'написал', 'сделал', 'создал', 'кодил']:
                    if maker_word in text.lower():
                        message_to_send = my_creator[random.randint(0, len(my_creator) - 1)]
                        my_prev_message[id] = message_to_send
                        return message_to_send
    for key in dict_lonely_messages.keys():
        for input_word in key.split('*'):
            if input_word in text.lower():
                message_to_send = dict_lonely_messages[key][random.randint(0, len(dict_lonely_messages[key]) - 1)]
                my_prev_message[id] = message_to_send
                return message_to_send
    message_to_send = nepon_words[random.randint(0, len(nepon_words) - 1)]
    my_prev_message[id] = message_to_send
    return message_to_send

def generate_comment(text, id, vk_session, owner_id):
    my_answer_to_axaxa = ['Рад, что смог насмешить', 'О, шуточка зашла))', 'Согласись, классный мем', 'Мем смешной ситуация смешная', 'Кажется, я научился шутить']
    if owner_id == -my_club_id:
        if 'хах' in text.lower() or if_l_elem_in_text(laughing_smiles, text.lower()):
            return my_answer_to_axaxa[random.randint(0, len(my_answer_to_axaxa) - 1)]

def full_address_geo(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}" \
                       "&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        return toponym_address + " имеет координаты: " + toponym_coodrinates
    else:
        return "Ошибка выполнения запроса:\n" + geocoder_request + f"\nHttp статус: {response.status_code} ({response.reason})"

def address_params(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    delta = "0.005"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    return map_params


def address_on_map(toponym_to_find):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=address_params(toponym_to_find))
    return BytesIO(response.content)


def org_address_on_map(toponym_to_find):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

    address_ll = address_params(toponym_to_find)["ll"]

    search_params = {
        "apikey": api_key,
        "text": toponym_to_find,
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        pass
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"][0]
    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    delta = "0.005"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        # позиционируем карту центром на наш исходный адрес
        "ll": address_ll,
        "spn": ",".join([delta, delta]),
        "l": "map",
        # добавим точку, чтобы указать найденную аптеку
        "pt": "{0},pm2dgl".format(org_point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return BytesIO(response.content)

def main():
    global vk_session
    vk_session = vk_api.VkApi(
        token='7055383a29abda93091360d8b3a41b8a9a63e267c1d8b858ec453afade6cd4a41e97a8fca387a45ce8ac2')
    longpoll = VkBotLongPoll(vk_session, my_club_id)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            reply_message(vk_session, event)
        elif event.type == VkBotEventType.PHOTO_COMMENT_NEW:
            print(event)
            print('Новый коммент:')
            print('Для меня от:', event.obj.comment['from_id'])
            print('Текст:', event.obj.comment['text'])
            reply_comment(vk_session, event)


if __name__ == '__main__':
    main()