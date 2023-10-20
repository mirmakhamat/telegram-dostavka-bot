from telegram import ReplyKeyboardMarkup, KeyboardButton
from bot import strings

def main_keyboard_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(strings.CONTACT_BTN),
            KeyboardButton(strings.ORDER_BTN)
        ],
        [
            KeyboardButton(strings.FEEDBACK_BTN),
            KeyboardButton(strings.SETTINGS_BTN)
        ]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
