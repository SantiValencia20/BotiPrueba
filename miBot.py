import telebot
from datetime import datetime
from telebot import types
import random 

# Token (Recuerda no compartirlo públicamente luego de tu prueba)
TOKEN = "8615140572:AAHypKSKumGbbRFMgz1lNR8k87PhHDZvAMw"
bot = telebot.TeleBot(TOKEN)

# Lista de respuestas aleatorias
respuestas_aleatorias = [
    "La Ciudad del Vaticano es el lugar con mayor consumo de vino per cápita del mundo.",
    "Ha nevado en el desierto del Sahara.",
    "Ya se hacer un Header ms rapido :D.",
    "La capital de Azerbaiyán, Bakú, está situada a 28 metros por debajo del nivel del mar.",
    "En ciudades como Longyearbyen (Noruega), está prohibido morir debido a que los cuerpos no se descomponen por el frío extremo",
    "La Torre Eiffel puede ser hasta 15 cm más alta en verano debido a la expansión térmica del hierro.",
    "Los bebés nacen con 300 huesos, pero al crecer se fusionan hasta tener 206.",
    "El mapa de GTA V es significativamente más grande que la isla de Manhattan en la vida real.",
    "A marzo de 2026, Minecraft se mantiene como el videojuego más vendido de todos los tiempos, superando los 300 millones de copias en múltiples plataformas.",
]

# Comando /start y /ayuda (ahora ambos activan el menú)
@bot.message_handler(commands=['start', 'ayuda'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # Definimos los botones exactamente como los vamos a comparar después
    btn_fecha = types.KeyboardButton('📅 Fecha')
    btn_hora = types.KeyboardButton('⏰ Hora')
    btn_ayuda = types.KeyboardButton('🆘 Ayuda')
    btn_DatoAleatorio = types.KeyboardButton('❓¿Dato Aleatorio?')
    
    markup.add(btn_fecha, btn_hora, btn_ayuda, btn_DatoAleatorio)
    
    texto = (
        "*¡Hola! Bienvenido a tu Bot de Prueba*\n\n"
        "Estoy listo para ayudarte. Usa los botones de abajo o escribe un comando como /fecha o /hora."
    )
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    texto_usuario = message.text

    # Verificamos Fecha
    if texto_usuario == '📅 Fecha' or texto_usuario == '/fecha':
        fecha = datetime.now().strftime("%d/%m/%Y")
        bot.send_message(message.chat.id, f"📅 *Hoy es:* `{fecha}`", parse_mode="Markdown")

    # Verificamos Dato Aleatorio
    elif texto_usuario == '¿Dato Aleatorio?' or texto_usuario.lower() == '/dato_aleatorio' or 'dato aleatorio' in texto_usuario.lower():
        dato_aleatorio = random.choice(respuestas_aleatorias)
        bot.send_message(message.chat.id, f"🎲 *¿Dato Aleatorio?*:\n\n{dato_aleatorio}", parse_mode="Markdown")

    # Verificamos Ayuda (Corregido el doble espacio)
    elif texto_usuario == '🆘 Ayuda' or texto_usuario == '/ayuda':
        bot.send_message(message.chat.id, "🆘 *Menú de Ayuda*:\n\n1. Presiona '📅 Fecha' para ver el día.\n2. Presiona '⏰ Hora' para ver la hora actual.\n3. Escribe 'Hola' para saludar.", parse_mode="Markdown") 

    # Verificamos Hora
    elif texto_usuario == '⏰ Hora' or texto_usuario == '/hora':
        hora = datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.chat.id, f"⏰ *La hora actual es:* `{hora}`", parse_mode="Markdown")
        
    # Saludo casual
    elif "hola" in texto_usuario.lower():
        bot.send_message(message.chat.id, "¡Hola! ¿En qué puedo ayudarte hoy?, puedes probar los botones que tienes abajo.")
        
    # Respuesta por defecto
    else:
        bot.send_message(message.chat.id, "No entiendo ese comando, intenta con los botones del menú.")

# Iniciar el bot
print("El bot está funcionando correctamente...")
bot.infinity_polling()