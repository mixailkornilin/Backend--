from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util import *
import json

#ИНИЦИАЛИЗАЦИЯ
dialog = Dialog()
dialog.mode = None
dialog.list = []
dialog.user = {}

# ID ГЕРОЕВ
HERO_IDS = {
    'abadon': 2,
    'axe': 7,
    'invoker': 39,
    'puck': 54,
    'shadow_shaman': 67,
    'legion_commander': 41,
    'juggernaut': 8,
}

HERO_NAMES_RU = {
    'abadon': 'Абадон',
    'axe': 'Акс',
    'invoker': 'Инвокер',
    'puck': 'Пак',
    'shadow_shaman': 'Тень Шамана',
    'legion_commander': 'Легионка',
    'juggernaut': 'Джаггернаут'
}

#ГОТОВЫЕ СБОРКИ
HERO_BUILDS = {
    'juggernaut': """🎮 **Джаггернаут**
    
🛡️ **Стартовые предметы:**
• Quelling Blade
• Tango
• Healing Salve
• Circlet
• Slippers of Agility

⚔️ **Ранняя игра:**
• Phase Boots
• Battle Fury
• Manta Style

💪 **Поздняя игра:**
• Abyssal Blade
• Butterfly
• Satanic
• Black King Bar
• Daedalus""",

    'abadon': """🎮 **Абадон**

🛡️ **Стартовые предметы:**
• Quelling Blade
• Tango
• Healing Salve
• Circlet
• Gauntlets of Strength

⚔️ **Ранняя игра:**
• Phase Boots
• Soul Ring
• Echo Sabre

💪 **Поздняя игра:**
• Assault Cuirass
• Abyssal Blade
• Heart of Tarrasque
• Black King Bar
• Satanic""",

    'axe': """🎮 **Акс**

🛡️ **Стартовые предметы:**
• Quelling Blade
• Tango
• Ring of Protection
• Circlet
• Healing Salve

⚔️ **Ранняя игра:**
• Phase Boots
• Blink Dagger
• Vanguard

💪 **Поздняя игра:**
• Blade Mail
• Crimson Guard
• Shiva's Guard
• Assault Cuirass
• Heart of Tarrasque""",

    'invoker': """🎮 **Инвокер**

🛡️ **Стартовые предметы:**
• Null Talisman
• Tango
• Faerie Fire
• Iron Branch

⚔️ **Ранняя игра:**
• Power Treads
• Urn of Shadows
• Aghanim's Scepter

💪 **Поздняя игра:**
• Black King Bar
• Octarine Core
• Refresher Orb
• Shiva's Guard
• Linken's Sphere""",

    'puck': """🎮 **Пак**

🛡️ **Стартовые предметы:**
• Null Talisman
• Tango
• Faerie Fire
• Iron Branch

⚔️ **Ранняя игра:**
• Power Treads
• Blink Dagger
• Eul's Scepter

💪 **Поздняя игра:**
• Aghanim's Scepter
• Shiva's Guard
• Dagon 5
• Octarine Core
• Black King Bar""",

    'shadow_shaman': """🎮 **Тень Шамана**

🛡️ **Стартовые предметы:**
• Gauntlets of Strength
• Tango
• Circlet
• Iron Branch
• Healing Salve

⚔️ **Ранняя игра:**
• Arcane Boots
• Blink Dagger
• Aether Lens

💪 **Поздняя игра:**
• Aghanim's Scepter
• Refresher Orb
• Octarine Core
• Black King Bar
• Shiva's Guard""",

    'legion_commander': """🎮 **Легионка**

🛡️ **Стартовые предметы:**
• Quelling Blade
• Tango
• Ring of Protection
• Circlet
• Healing Salve

⚔️ **Ранняя игра:**
• Phase Boots
• Blink Dagger
• Blade Mail

💪 **Поздняя игра:**
• Desolator
• Assault Cuirass
• Daedalus
• Black King Bar
• Heart of Tarrasque"""
}


async def fetch_hero_build(hero_key):
    """Возвращает готовую сборку"""
    return HERO_BUILDS.get(hero_key, "❌ Сборка не найдена")


#ГЛАВНОЕ МЕНЮ 
async def start(update, context):
    dialog.mode = "start"

    keyboard = [
        [InlineKeyboardButton("🛡️ Узнай что собирать на героя", callback_data='menu_hero')],
        [InlineKeyboardButton("📊 Узнай вин-рейт героя", callback_data='menu_winrate')],
        [InlineKeyboardButton("🏆 Узнай лучшего героя", callback_data='menu_top')],
        [InlineKeyboardButton("📰 Новости про Pro команду", callback_data='menu_pro')],
        [InlineKeyboardButton("📋 Выбери патч", callback_data='menu_patch')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("⚔️ Dota 2 Bot - Главное меню:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("⚔️ Dota 2 Bot - Главное меню:", reply_markup=reply_markup)


# ============== МЕНЮ ГЕРОЕВ ==============
async def hero_menu(update, context):
    dialog.mode = "hero"

    keyboard = [
        [InlineKeyboardButton("🔙 Вернуться в меню", callback_data='back_to_menu')],
        [
            InlineKeyboardButton("🛡️ Abadon", callback_data='hero_abadon'),
            InlineKeyboardButton("🪓 Axe", callback_data='hero_axe')
        ],
        [
            InlineKeyboardButton("🧙 Invoker", callback_data='hero_invoker'),
            InlineKeyboardButton("🧚 Puck", callback_data='hero_puck')
        ],
        [
            InlineKeyboardButton("🐍 Shadow Shaman", callback_data='hero_shadow_shaman'),
            InlineKeyboardButton("⚔️ Legion Commander", callback_data='hero_legion_commander')
        ],
        [
            InlineKeyboardButton("⚔️ Juggernaut", callback_data='hero_juggernaut'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text("🎮 Выбери героя:", reply_markup=reply_markup)




# ОБРАБОТЧИК КНОПОК 
async def button_callback(update, context):
    query = update.callback_query
    await query.answer()

    print(f"✅ Нажата кнопка: {query.data}")

    if query.data == 'menu_hero':
        await hero_menu(update, context)

    elif query.data == 'back_to_menu':
        await start(update, context)

    elif query.data.startswith('hero_'):
        hero_key = query.data.replace('hero_', '')
        hero_name = HERO_NAMES_RU.get(hero_key, hero_key)

        # Показываем загрузку
        await query.edit_message_text(f"⏳ Загружаем сборку для {hero_name}...")

        # Получаем данные
        build_text = await fetch_hero_build(hero_key)

        # Показываем результат
        await query.edit_message_text(build_text, parse_mode='Markdown')

        # Кнопки после сборки
        keyboard = [
            [InlineKeyboardButton("🔙 К героям", callback_data='menu_hero')],
            [InlineKeyboardButton("🏠 Главное меню", callback_data='back_to_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Что делаем дальше?",
            reply_markup=reply_markup
        )


#ЗАПУСК
app = ApplicationBuilder().token("8533401351:AAFV4DFLPP0G6Wud14uH6QOSliTm0IygZfM").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
lambda u, c: send_text(u, c, "Используй кнопки меню! 👆")))
app.run_polling()
