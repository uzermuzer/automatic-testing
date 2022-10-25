from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    btn = browser.find_element(By.ID,"book")
    btn.click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    int1 = browser.find_element(By.ID,"input_value")
    x = int1.text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    submit = browser.find_element(By.ID, "solve").click()


finally:

    time.sleep(15)

    browser.quit()

