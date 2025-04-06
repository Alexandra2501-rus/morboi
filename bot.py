from queue import Queue  # Импортируем стандартную очередь

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler

# Токен бота
TOKEN = '7958321662:AAHO9D2simqHTWHHjnZ-QUYDQRKVdUHXILQ'

# URL игры
GAME_URL = 'https://example.com/your-game.html'


def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    update.message.reply_text('Привет! Хочешь поиграть в Морской бой? Нажми /play.')


def play_game(update: Update, context: CallbackContext) -> None:
    """Отправляет игру пользователю"""
    bot = context.bot
    chat_id = update.effective_chat.id
    bot.send_game(
        chat_id=chat_id,
        game_short_name=GAME_URL,
        disable_web_page_preview=True
    )


def main() -> None:
    """Запуск бота"""
    update_queue = Queue()  # Создаем очередь для обновлений

    application = ApplicationBuilder().token(TOKEN).update_queue(update_queue).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('play', play_game))

    # Запуск бота
    application.run_polling()

    # Сообщение о запуске бота
    print("Бот запущен!")


if __name__ == '__main__':
    main()