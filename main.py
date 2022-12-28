# bot.stop_polling()
def ziz(message):
    bot.send_message(message.from_user.id, "Программа отработала. Для повторного запуска введите /start",reply_markup=ReplyKeyboardRemove())


def ol(unk, pon):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mn = types.KeyboardButton("Понедельник")
    tu = types.KeyboardButton("Вторник")
    wdn = types.KeyboardButton("Среда")
    thu = types.KeyboardButton("Четверг")
    fr = types.KeyboardButton("Пятница")
    std = types.KeyboardButton("Суббота")
    sun = types.KeyboardButton("Воскресенье")
    markup.add(mn, tu, wdn, thu, fr, std, sun)
    bot.send_message(unk.chat.id, 'Выберите день недели', reply_markup=markup)
    bot.register_next_step_handler(unk, pon)


from operator import itemgetter
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
bot = telebot.TeleBot('5929215785:AAGPmEby5tQxCl8HwFraCVEd6SxbIfafQag')
week = \
    {
        'Понедельник': 'MN.txt',
        'Вторник': 'TUE.txt',
        'Среда': 'WDN.txt',
        'Четверг': 'THU.txt',
        'Пятница': 'FR.txt',
        "Суббота": 'STD.txt',
        'Воскресенье': 'SUN.txt'
    }
@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Чтение")
    item2 = types.KeyboardButton("Добавление")
    item3 = types.KeyboardButton("Замена")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Чтение":
        ol(message, op_text)
    elif message.text == "Добавление":
        ol(message, ev)
    elif message.text == "Замена":
        ol(message, ev_sec)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда, напишите /start')

def op_text(message):
    day = message.text
    x = week[str(day)]
    with open(x, 'r', encoding='utf-8') as my_f:
        for lin in my_f:
            bot.send_message(message.from_user.id, lin)
    ziz(message)


def ev(message):
    global day
    day = message.text
    bot.send_message(message.from_user.id, 'Укажите время и мероприятие, через пробел.Например "18:00 Ужин" ')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    event = message.text
    x = week[str(day)]
    with open(x, 'a', encoding='utf-8') as my_f:
        my_f.write(str(event))
        my_f.write('\n')
    ziz(message)


def ev_sec(message):
    global day
    day = message.text
    bot.send_message(message.from_user.id, 'Укажите время и мероприятие, через пробел.Например "18:00 Ужин" ')
    bot.register_next_step_handler(message, chang)


def chang(message):
    event = message.text
    x = week[day]
    with open(x, 'w', encoding='utf-8') as my_f:
        my_f.write(event)
        my_f.write('\n')
    ziz(message)


bot.infinity_polling()
