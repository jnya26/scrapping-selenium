from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import traceback
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


class SocialNetworkScrapper:

    BASE_URL = f"{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_POST}"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    REGISTER_URL = f"{BASE_URL}/auth/register"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self):
        self.driver = None


    def create_driver(self):
        try:
            install_dir = "/snap/firefox/current/usr/lib/firefox"
            driver_loc = os.path.join(install_dir, "geckodriver")
            binary_loc = os.path.join(install_dir, "firefox")

            service = FirefoxService(driver_loc)
            opts = webdriver.FirefoxOptions()
            opts.binary_location = binary_loc

            self.driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH, service=service, options=opts)
            return self.driver

        except Exception as e:
            traceback.print_exc()

    def social_network_register(self):
        driver = self.create_driver()
        driver.get(self.REGISTER_URL)

        username_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        email_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        email_elem.send_keys(config.SOCIAL_NETWORK_EMAIL)

        password_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        confirm_password_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='confirm_password']")
        confirm_password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        confirm_password_elem.send_keys(keys.Keys.ENTER)



    def social_network_login(self):
        self.social_network_register()
        time.sleep(2)
        self.driver.get(self.LOGIN_URL)

#"//div[@class='form-group']/input[@id='username']" - find all tahs with classes "form-group(in browser)"
# https://www.w3schools.com/xml/xpath_syntax.asp - tutorial

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        password_elem.send_keys(keys.Keys.ENTER)


    def create_post(self, login_required=True):
        time.sleep(2)
        blog_page = self.driver.find_element(By.LINK_TEXT, "Blog").click()

        title_elem = self.driver.find_element(By.ID, "inputTitle")
        title_elem.send_keys('New title post from Jenya1')

        text_elem = self.driver.find_element(By.ID, "inputText")
        text_elem.send_keys('New content text from Jenya1. Thaks for attention.')
        time.sleep(2)

        create_post_button = self.driver.find_element(By.XPATH, "//div/button[@class='btnd']").click()
        time.sleep(2)
        like_button = self.driver.find_element(By.XPATH, "//div/a[1]/button[1]").click()
        time.sleep(2)
        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout").click()