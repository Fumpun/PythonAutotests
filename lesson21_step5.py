from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    print(x)
    y = calc(x)
    print(y)

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    rcheck = browser.find_element_by_css_selector('#robotCheckbox')
    rcheck.click()
    rRule = browser.find_element_by_css_selector('#robotsRule')
    rRule.click()
    submit = browser.find_element_by_css_selector('[type = "submit"]')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

