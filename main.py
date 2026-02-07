# Импорт load_dotenv.
from dotenv import load_dotenv

# Импорт библиотеки для работы с окружением.
import os

# Загрузка переменных из .env
load_dotenv(dotenv_path='.env')

print('Hello from repository!')

def print_author():
    author = os.getenv('AUTHOR')
    # Допишите здесь ваш код
    print(f"Автор проекта: {author}")

# Не забудьте вызвать функцию, чтобы увидеть результат
print_author()
