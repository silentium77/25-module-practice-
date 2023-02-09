import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/zimin/PycharmProjects/tests/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, "email").send_keys('ziminajn90@outlook.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys('12345678')
    time.sleep(5)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(5)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(5)
    # Нажимаем на кнопку "Мои Питомцы"
    pytest.driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
    time.sleep(5)
    #
    pytest.driver.find_element(By.CSS_SELECTOR, '#all_my_pets table tbody tr')
    all_my_pets_number = pytest.driver.find_element(By.XPATH, '//div[contains(@class, ".col-sm-4 left")]/text()[2]')
