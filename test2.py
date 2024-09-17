import aiohttp
import asyncio
import hashlib
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])


def hash_data(data):
    """Хеширование."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


async def fetch_data(url, token, page, limit):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    params = {
        'page': page,
        'limit': limit
    }

    # Логирование хеши
    logging.info(f'Отправка запроса: '
                 f'URL: {hash_data(url)}, Token: {hash_data(token)}, Page: {page}, Limit: {limit}')

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, params=params) as response:
                # Логирование
                logging.info(f'Получен ответ с кодом: {response.status}')

                if response.status != 200:
                    error_data = await response.json()
                    error_message = error_data.get('error', 'Неизвестная ошибка')
                    logging.error(f'Ошибка {response.status}: {error_message}')
                    raise Exception(f'Ошибка {response.status}: {error_message}')

                # ответ
                data = await response.json()

                # Логирование хешированных данных ответа
                logging.info(f'Успешный ответ. Хеш данных: {hash_data(str(data))}')
                return data

        except aiohttp.ClientError as e:
            logging.error(f'Произошла ошибка запроса: {str(e)}')
        except Exception as e:
            logging.error(f'Произошла ошибка: {str(e)}')


# Пример
async def main():
    url = ''
    token = 'токен'
    page = 1
    limit = 10

    data = await fetch_data(url, token, page, limit)
    if data:
        logging.info(f'Полученные данные: {data}')


# Запуск
asyncio.run(main())
