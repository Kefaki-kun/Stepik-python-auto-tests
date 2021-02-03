from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    book_button = browser.find_element_by_id("book")
    book_button_2 = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button.click()
    num1 = browser.find_element_by_id("input_value")
    num1 = num1.text
    x=int(num1)
    y=calc(x)
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(y)
	
	# Отправляем заполненную форму
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()