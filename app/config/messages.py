from app.config.commands import commands


class MESSAGES:
    # Загружаем список команд
    commands_list = [f'/{command} -> {description}' for command, description in commands.items()]
    commands_text = '\n'.join(commands_list)

    help = f'Команды:\n' \
           f'{commands_text}'

    start = (
        '👋 Привет! Я - робот компании "АртСад".\n\n'
        'Я умею показывать фотографии взрослых растений из нашего прайса 🌿, '
        'а также их краткое описание, чтобы вам было проще определиться с выбором.\n\n'
        'Выберите растение из каталога: /catalog 📚'
    )

    admin = "Панель администратора"

    developer = "Роман @y3841"

    catalog = 'Выбери растение 👇\n'

    category = 'Выбери категорию 👇\n'

    # CONTACTS
    contacts = (
        '📍 Самара, Южное шоссе, 1/1,\n'
        'Рынок "Солнечный" 🏢\n'
        'Ежедневно с 08:00 до 20:00 ⏰'
    )
    phone_1 = "+79199133122"
    name = "АртСад"
