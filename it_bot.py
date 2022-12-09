from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from citilink import *
import time
import utils as ut

bot = Bot(token='your_token', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
CHANNEL_ID = 'your_channel_id'
NOT_SUB_MESSAGE = 'Для доступа к функционалу, подпишитесь на канал'


# def create_card(data):
#     for index, i in enumerate(data):
#
#         card = f'{hbold(i.get("name"))}\n' \
#                f'{hbold(i.get("price") + " ₽")}\n' \
#                f'{i.get("link")}'
#
#         if index % 20 == 0:
#             time.sleep(3)
#
#         return card

def sub_check_channel(chat_member):  # Проверка на подписку
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    if message.chat.type == 'private':
        if sub_check_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = types.KeyboardButton(text="Начать")

            keyboard.add(button_1)
            await message.answer(
                'Рады вас видеть! Этот бот создан для быстрого поиска товара со скидкой из магазина Ситиилнк',
                reply_markup=keyboard)
        else:
            await message.answer(NOT_SUB_MESSAGE, reply_markup=ut.sub_menu)


@dp.message_handler(Text(equals='Начать'))
async def get_choice(message: types.Message):
    if sub_check_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Процессоры", "Видеокарты", "Материнские платы"]
        keyboard.add(*buttons)
        await message.answer('Какие комплектующие вас интересуют?', reply_markup=keyboard)
    else:
        await message.answer(NOT_SUB_MESSAGE, reply_markup=ut.sub_menu)


@dp.callback_query_handler(text='subchanneldone')  # Что будет выводиться, если человек подписан
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id)
    if sub_check_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Процессоры", "Видеокарты", "Материнские платы"]
        keyboard.add(*buttons)
        await message.answer('Какие комплектующие вас интересуют?', reply_markup=keyboard)
    else:
        await message.answer(NOT_SUB_MESSAGE, reply_markup=ut.sub_menu)

# начало numbers
# начало процессоры

# def create_card(data):
#     for index, i in enumerate(data):
#         card = f'{hbold(i.get("name"))}\n' \
#                f'{hbold(i.get("price") + " ₽")}\n' \
#                f'{i.get("link")}'
#         if index % 20 == 0:
#             time.sleep(3)
#         return card

@dp.message_handler(Text(equals='Процессоры'))
async def get_numbers(message: types.Message):
    num_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num_buttons = ['10', '30', '50', 'все', 'Назад⬅️']  # сколько карточкек будет показываться
    num_keyboard.add(*num_buttons)
    await message.answer('Сколько карточек хочешь увидеть?', reply_markup=num_keyboard)

    @dp.message_handler(Text(equals='10'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        CPU()
        count = 0

        with open('CPU_citilink5%.json') as file:

            data = json.load(file)[:10]

            for index, i in enumerate(data):
                card = f'{hbold(i.get("name"))}\n' \
                       f'{hbold(i.get("price") + " ₽")}\n' \
                       f'{i.get("link")}'
                if index % 20 == 0:
                    time.sleep(3)

                await message.answer(card)
                print(count)

    @dp.message_handler(Text(equals='30'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        CPU()
        count = 0
        with open('CPU_citilink5%.json') as file:
            data = json.load(file)[:30]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            count += 1
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)
            print(count)

    @dp.message_handler(Text(equals='50'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        CPU()
        count = 0
        with open('CPU_citilink5%.json') as file:
            data = json.load(file)[:50]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            count += 1
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)
            print(count)

    @dp.message_handler(Text(equals='все'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        CPU()
        count = 0
        with open('CPU_citilink5%.json') as file:
            data = json.load(file)
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            count += 1
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)
            print(count)


# конец процессоры

# начало видеокарты
@dp.message_handler(Text(equals='Видеокарты'))
async def get_numbers(message: types.Message):
    num_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num_buttons = ['10', '30', '50', 'все', 'Назад⬅️']
    num_keyboard.add(*num_buttons)
    await message.answer('Сколько карточек хочешь увидеть?', reply_markup=num_keyboard)

    @dp.message_handler(Text(equals='10'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        video_cards()

        with open('Video_cards_citilink5%.json') as file:
            data = json.load(file)[:10]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)

    @dp.message_handler(Text(equals='30'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        video_cards()
        count = 0
        with open('Video_cards_citilink5%.json') as file:
            data = json.load(file)[:30]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            count += 1
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)
            print(count)

    @dp.message_handler(Text(equals='50'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        video_cards()

        with open('Video_cards_citilink5%.json') as file:
            data = json.load(file)[:50]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)

    @dp.message_handler(Text(equals='все'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        video_cards()

        with open('Video_cards_citilink5%.json') as file:
            data = json.load(file)
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)


# конец видеокарты

# начало motherboard
@dp.message_handler(Text(equals='Материнские платы'))
async def get_numbers(message: types.Message):
    num_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num_buttons = ['10', '30', '50', 'все', 'Назад⬅️']
    num_keyboard.add(*num_buttons)
    await message.answer('Сколько карточек хочешь увидеть?', reply_markup=num_keyboard)

    @dp.message_handler(Text(equals='10'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        motherboard()

        with open('motherboard_citilink5%.json') as file:
            data = json.load(file)[:10]

    @dp.message_handler(Text(equals='30'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        motherboard()
        count = 0
        with open('motherboard_citilink5%.json') as file:
            data = json.load(file)[:30]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            count += 1
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)
            # print(count)

    @dp.message_handler(Text(equals='50'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        motherboard()

        with open('motherboard_citilink5%.json') as file:
            data = json.load(file)[:50]
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)

    @dp.message_handler(Text(equals='все'))
    async def result(message: types.Message):
        await message.answer('Ищем лучшее для вас')

        motherboard()

        with open('motherboard_citilink5%.json') as file:
            data = json.load(file)
        for index, i in enumerate(data):
            card = f'{hbold(i.get("name"))}\n' \
                   f'{hbold(i.get("price") + " ₽")}\n' \
                   f'{i.get("link")}'
            if index % 20 == 0:
                time.sleep(3)
            await message.answer(card)


# Конец motherboard

@dp.message_handler(commands=['about_us'])
async def connection(message: types.Message):
    await message.answer('Вот кого ты ищешь - https://t.me/KkkkkkkkKfh')


@dp.message_handler(commands=['show_categories'])
async def show_categories(message: types.Message):
    await get_choice(message)


@dp.message_handler(Text(equals='Назад⬅️'))
async def nazad(message: types.Message):
    await show_categories(message)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
