# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class create_order(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_create_order(self):
        success = True
        wd = self.wd
        wd.get("http://alpha.mamsy.ru/")
        wd.find_element_by_link_text("Вход здесь").click()
        wd.find_element_by_id("input-login_mail").click()
        wd.find_element_by_id("input-login_mail").clear()
        wd.find_element_by_id("input-login_mail").send_keys("nikolaeva.m@mamsycorp.ru")
        wd.find_element_by_id("input-login_pass").click()
        wd.find_element_by_id("input-login_pass").clear()
        wd.find_element_by_id("input-login_pass").send_keys("hu44QWERTY88")
        wd.find_element_by_xpath("//form[@id='login_account']//button[.='Войти']").click()
        wd.find_element_by_xpath("//div[@class='content']/div[3]/div/div/div[3]/div[1]/a/div[1]/div[1]/img[2]").click()
        wd.find_element_by_css_selector("img.product_grid__img").click()
        wd.find_element_by_xpath("//div[@class='product_right']//div[.='44']").click()
        wd.find_element_by_xpath("//div[@class='jsProductCardAddToCart']/input").click()
        wd.find_element_by_link_text("Перейти в корзину").click()
        wd.find_element_by_id("checkout_button").click()
        wd.find_element_by_id("customers_telephone").click()
        wd.find_element_by_id("customers_telephone").clear()
        wd.find_element_by_id("customers_telephone").send_keys("+7(989)898-98-98")
        wd.find_element_by_css_selector("span.pay_block.payCash").click()
        if not wd.find_element_by_id("payment-box_cash").is_selected():
            wd.find_element_by_id("payment-box_cash").click()
        wd.find_element_by_id("entry_exact_street_address").click()
        wd.find_element_by_id("entry_exact_street_address").clear()
        wd.find_element_by_id("entry_exact_street_address").send_keys("TEST")
        wd.find_element_by_id("entry_home_address").click()
        wd.find_element_by_id("entry_home_address").clear()
        wd.find_element_by_id("entry_home_address").send_keys("4")
        wd.find_element_by_id("entry_flat_address").click()
        wd.find_element_by_id("entry_flat_address").clear()
        wd.find_element_by_id("entry_flat_address").send_keys("4")
        wd.find_element_by_id("order_products_button").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
