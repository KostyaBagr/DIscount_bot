from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton\



BtnUrlChannel = InlineKeyboardButton(text='Подписаться', url = 'your_channel_url')

btnDoneSub = InlineKeyboardButton(text = 'Подписался', callback_data = 'subchanneldone')

sub_menu = InlineKeyboardMarkup(row_width =1)

sub_menu.insert(BtnUrlChannel)
sub_menu.insert(btnDoneSub)

