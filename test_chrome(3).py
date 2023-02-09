import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/zimin/PycharmProjects/tests/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_name_age_of_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys('ziminajn90@outlook.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys('12345678')
   time.sleep(2)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   time.sleep(2)
   # Нажимаем на кнопку "Мои питомцы"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
   time.sleep(2)
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

   all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
   print(len(all_pets))





