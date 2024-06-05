import telegram as tg
import telegram.ext as tge
import random as rn

TOKEN = '7008079892:AAHC2kvgShjLBho9WwY6drc0e98Gh6l8oF0'

async def start(update: tg.Update, context: tge.CallbackContext) -> None:
    reply_markup = tg.InlineKeyboardMarkup(
        [[tg.InlineKeyboardButton('Продолжить', callback_data='continue')]],
    )
    await update.message.reply_text('Привет, если ты стал жертвой кибербуллинга, ты попал в нужное место. '
                                    'Жми продолжить, чтобы узнать больше 👇🏻',reply_markup=reply_markup)

async def give_description(update: tg.Update, context: tge.CallbackContext) -> None:
    description = ('<b>Кибербуллинг</b> — преследование сообщениями, содержащими оскорбления, агрессию, запугивание; '
                   'хулиганство; социальное бойкотирование с помощью различных интернет-сервисов.')
    reply_markup = tg.InlineKeyboardMarkup([[tg.InlineKeyboardButton('Как мне бороться с кибербулингом?',
                                                                     callback_data='help')]])
    photo_url = 'https://static.tildacdn.com/tild6564-6566-4162-a365-383063633036/Frame_5-2.jpg'
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=description,
                                 parse_mode='HTML', reply_markup=reply_markup)

async def give_advices(update: tg.Update, context: tge.CallbackContext) -> None:
    gratitude_list = [
        "Спасибо большое за помощь.",
        "Спасибо за вашу помощь!",
        "Большое спасибо за поддержку.",
        "Благодарю вас за помощь.",
        "Спасибо за ваше участие.",
        "Огромное спасибо за вашу поддержку.",
        "Спасибо за ваш вклад.",
        "Благодарю вас за вашу помощь.",
        "Спасибо за ваше внимание.",
        "Спасибо за вашу заботу.",
        "Благодарю вас за ваше время и усилия."
    ]

    advices = ('<b>Основные советы по борьбе с кибербуллингом:</b>\n\n'
                '<b>1.</b> Не бросайся в бой. Лучший способ: посоветоваться как себя вести и, если нет того, '
                'к кому можно обратиться, то вначале успокоиться. Если ты начнешь отвечать оскорблениями на оскорбления, '
                'то только еще больше разожжешь конфликт.\n\n' 
                '<b>2.</b> Управляй своей киберрепутацией.\n\n'
                '<b>3.</b> Анонимность в сети мнимая. Существуют способы выяснить, кто стоит за анонимным аккаунтом.\n\n'
                '<b>4.</b> Не стоит вести хулиганский образ виртуальной жизни. Интернет фиксирует все твои действия и '
                'сохраняет их. Удалить их будет крайне затруднительно.\n\n'
                '<b>5.</b> Соблюдай свой виртуальную честь смолоду.\n\n'
                '<b>6.</b> Игнорируй единичный негатив. Одноразовые оскорбительные сообщения лучше игнорировать. '
                'Обычно агрессия прекращается на начальной стадии.\n\n'
                '<b>7.</b> Бан агрессора. В программах обмена мгновенными сообщениями, в социальных сетях '
                'есть возможность блокировки отправки сообщений с определенных адресов.\n\n'
                '<b>8.</b> Если ты свидетель кибербуллинга. Твои действия: выступить против преследователя, показать ему, что его '
               'действия оцениваются негативно, поддержать жертву, которой нужна психологическая помощь, сообщить взрослым о факте агрессивного поведения в сети.')
    reply_markup = tg.ReplyKeyboardMarkup([[gratitude_list[rn.randint(0, 10)]]], one_time_keyboard=True,
                                          resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=advices, reply_markup=reply_markup,
                                   parse_mode='HTML')

async def send_greet(update: tg.Update, context: tge.CallbackContext) -> None:
    photo_path = 'workProjects/photo_2024-05-30_01-22-54.jpg'
    reply_markup = tg.ReplyKeyboardMarkup([['До свидания👋🏻']], one_time_keyboard=True,
                                          resize_keyboard=True)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_path,
                                 caption='Пожалуйста, обращайся, если что-то случится. '
                                        'Будем рад помочь тебе еще раз. Пока! 👋🏻')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Контакты для круглосуточной поддержки: '
                                                                          '@karebaviktoriia @aleenkiy',
                                   reply_markup=reply_markup)

async def bye(update: tg.Update, context: tge.CallbackContext) -> None:
    reply_markup = tg.InlineKeyboardMarkup([[tg.InlineKeyboardButton('Вернуться к советам',
                                                                     callback_data='help')]])
    variations = [
        'Если что-то случится, обращайся. Будем рады помочь тебе еще раз. Пока! 👋🏻',
        'Хорошего Вам дня! Обращайтесь.',
        'До встречи! Надеемся, что вам помогли наши советы.',
        'Пока-пока!',
        'До свидания!'
    ]
    await update.message.reply_text(variations[rn.randint(0, 4)], reply_markup=reply_markup)

regex_condition = ('(Спасибо за вашу помощь!)|(Большое спасибо за поддержку.)|(Благодарю вас за помощь.)|(Спасибо за '
                   'ваше участие.)|(Огромное спасибо за вашу поддержку.)|(Спасибо за ваш вклад.)|(Благодарю вас за вашу '
                   'помощь.)|(Спасибо за ваше внимание.)|(Спасибо за вашу заботу.)|(Благодарю '
                   'вас за ваше время и усилия.)')

def main() -> None:

    application = tge.Application.builder().token(TOKEN).build()

    application.add_handler(tge.CommandHandler("start", start))
    application.add_handler(tge.CallbackQueryHandler(give_description, pattern='continue'))
    application.add_handler(tge.CallbackQueryHandler(give_advices, pattern='help'))
    application.add_handler(tge.MessageHandler(tge.filters.Regex(regex_condition), send_greet))
    application.add_handler(tge.MessageHandler(tge.filters.Regex('До свидания👋🏻'), bye))

    application.run_polling(allowed_updates=tg.Update.ALL_TYPES)

if __name__ == '__main__':
    main()
