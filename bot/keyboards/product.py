from telegram import ReplyKeyboardMarkup, KeyboardButton
from db.functions import product as product_functions

from bot import strings

def product_keyboard_markup(category_id) -> ReplyKeyboardMarkup:
    products = product_functions.get_products_by_category(category_id)
    keyboard = []
    tmp = []
    for product in products:
        tmp.append(KeyboardButton(product.name))
        if len(tmp) == 2:
            keyboard.append(tmp)
            tmp = []
    
    if len(tmp) != 0:
        keyboard.append(tmp)

    keyboard.append([KeyboardButton(strings.BACK_BTN)])

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def product_count_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3')],
        [KeyboardButton('4'), KeyboardButton('5'), KeyboardButton('6')],
        [KeyboardButton('7'), KeyboardButton('8'), KeyboardButton('9')],
        [KeyboardButton(strings.BACK_BTN)]
    ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)