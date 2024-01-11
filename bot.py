import random
import telebot
from telebot import types

TOKEN = open('token.conf', 'r').read().strip()
bot = telebot.TeleBot(TOKEN)

start_msg = (
    '🧵 <b>Olá, {}</b>\n'
    'Sou um bot que funciona em grupos e supergrupos.\n\n'
    '🕹 <b>Instruções de uso</b>\n'
    'Adicione-me em um grupo sem tópicos. Utilize o símbolo <code>#</code> no início de uma mensagem e irei enviar o link da thread.\n'
    'Caso eu seja colocado como administrador do grupo, as mensagens serão fixadas.\n'
    'Administradores do grupo podem usar o comando <code>/unpin</code> para desafixar uma thread.\n\n'
    '💵 <b>Ajude com os custos</b>\n'
    'Gostou? Faça um PIX e ajude com os custos de hospedagem.\n'
    'Chave PIX: <code>bots@grf.xyz</code>\n\n'
    '⚙️ <b>Repositório</b>\n'
    'https://github.com/GabrielRF/ThreadLinkBot'
)
emoji = ['🧵', '💬', '💭', '🗯', '🗣', '🧶', '📋', '📜', '🗒', '📝']

def is_admin(chat_id, user_id):
    status = bot.get_chat_member(
        chat_id,    
        user_id
    ).status
    if user_id == 1087968824:
        return True
    if status in ['creator', 'administrator']:
        return True
    return False

@bot.message_handler(commands=['unpin'])
def unpin_command(message):
    if is_admin(message.chat.id, message.from_user.id):
        try:
            bot.unpin_chat_message(
                message.chat.id,
                message.message_thread_id+1
            )
            bot.delete_message(message.chat.id, message.id)
        except:
            pass

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id > 0:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.reply_to(
            message,
            start_msg.format(message.from_user.first_name),
            parse_mode='HTML'
        )

@bot.message_handler(
    func=lambda message: 'group' in message.chat.type
    and not message.chat.is_forum
)
def group_message(message):
    if not message.message_thread_id and '#' in message.text[0]:
        group_id = str(message.chat.id).replace('-100', '')
        link = f'https://t.me/c/{group_id}/{message.id}?thread={message.id}'
        button = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(
            f'Thread {random.choice(emoji)}',
            url=link
        )
        button.row(btn)
        msg = bot.reply_to(
            message,
            message.text.replace('#', ''),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=button
        )
        try:
            bot.pin_chat_message(
                message.chat.id,
                msg.id,
                disable_notification=True
            )
            bot.delete_message(message.chat.id, msg.id+1)
        except:
            pass

if __name__ == "__main__":
    bot.infinity_polling()
