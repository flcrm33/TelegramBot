from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton('/Слава_Україні')
b2 = KeyboardButton('/Слава_Нації')
b3 = KeyboardButton('/Меню')
#b4 = KeyboardButton('Поділитись номером', request_contact=True)
#b5 = KeyboardButton('Де я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)#.row(b4, b5)
