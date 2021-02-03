from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    second_window=browser.window_handles[1] #получаем второе окно
    second_window=browser.switch_to.window(second_window) #переключаемся на второе окно
    num = browser.find_element_by_id("input_value")
    num = num.text
    x=int(num)
    y=calc(x)
    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()