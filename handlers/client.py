from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Слава Україні')
        await message.delete()
    except:
        await message.reply("Спілкування з помічником через ОП, напишіть йому:\nhttps://t.me/Per_Assist_bot")


# @dp.message_handler(commands=['Слава_Україні'])
async def command_gloryofukraine(message: types.Message):
    await bot.send_message(message.from_user.id, 'Героям Слава')


# @dp.message_handler(commands=['Слава_Нації'])
async def command_gloryofnation(message: types.Message):
    await bot.send_message(message.from_user.id, 'Смерть ворогам')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_gloryofukraine, commands=['Слава_Україні'])
    dp.register_message_handler(command_gloryofnation, commands=['Слава_Нації'])
