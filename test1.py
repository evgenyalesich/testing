import aiohttp
import asyncio


# GET-запрос
async def get_request():
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            print(result)


# POST-запрос
async def post_request():
    url = 'https://httpbin.org/post'
    data = {"name": "John", "age": 30}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            print(f"Status code: {response.status}")


# GET-запрос с параметрами
async def get_request_with_params():
    url = 'https://jsonplaceholder.typicode.com/comments'
    params = {'userId': 1}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            result = await response.text()
            print(result)


# GET-запрос для получения заголовков
async def get_headers():
    url = 'https://httpbin.org/headers'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            headers = response.headers
            print(headers)


# PUT-запрос
async def put_request():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    data = {"title": "foo", "body": "bar", "userId": 1}
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=data) as response:
            result = await response.text()
            print(result)


# DELETE-запрос
async def delete_request():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            if response.status == 200:
                print(f"Successfully deleted, status code: {response.status}")


# GET-запрос с таймаутом
async def get_request_with_timeout():
    url = 'https://httpbin.org/delay/10'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                result = await response.text()
                print(result)
    except asyncio.TimeoutError:
        print("Request timed out")


# запрос для получения только значения поля 'url' из JSON-ответа
async def get_url_field():
    url = 'https://httpbin.org/get'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            print(result['url'])


# GET-запрос для проверки наличия поля 'userId'
async def check_userId_field():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            if 'userId' in result:
                print("Field 'userId' is present in the response")


# вызов всех запросов
async def main():
    await get_request()
    await post_request()
    await get_request_with_params()
    await get_headers()
    await put_request()
    await delete_request()
    await get_request_with_timeout()
    await get_url_field()
    await check_userId_field()


# Запуск
if __name__ == '__main__':
    asyncio.run(main())
