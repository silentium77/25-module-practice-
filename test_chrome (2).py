import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/zimin/PycharmProjects/tests/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('ziminajn90@outlook.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345678')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


images = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-img-top')
names = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-title')
descriptions = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-text')

for i in range(len(names)):
    assert images[i].get_attribute('src') != ''
    assert names[i].text != ''
    assert descriptions[i].text != ''
    assert ', ' in descriptions[i]
    parts = descriptions[i].text.split(", ")
    assert len(parts[0]) > 0
    assert len(parts[1]) > 0
