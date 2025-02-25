import time
import asyncio
from apify import Actor
from playwright.async_api import async_playwright


async def get_strava_cookies():
    async with async_playwright() as p:
        # Запускаем браузер
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Переходим на страницу авторизации Strava
        await page.goto('https://www.strava.com/login')

        # Заполняем поля для авторизации (замените на свои данные)
        await page.fill('input[name="email"]', 'YOUR_EMAIL')
        await page.fill('input[name="password"]', 'YOUR_PASSWORD')

        # Нажимаем кнопку для входа
        await page.click('button[type="submit"]')

        # Ждем, пока страница загрузится после авторизации
        await page.wait_for_navigation()

        # Получаем cookies
        cookies = await page.context.cookies()

        # Закрываем браузер
        await browser.close()

        return cookies


async def main():
    cookies = await get_strava_cookies()
    print(cookies)
    # Вы можете сохранить cookies в Dataset или обработать их для дальнейшего использования
    await Actor.push_data(cookies)


if __name__ == '__main__':
    asyncio.run(main())
