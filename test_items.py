from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket").is_enabled()
    assert submit_button, "Кнопка не обнаружена"

