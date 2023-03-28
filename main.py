from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import random
import os

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
ACCOUNT_URL = os.environ.get("ACCOUNT_URL")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self, path):
        service = ChromeService(executable_path=path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        self.driver.get(url=INSTAGRAM_URL)
        time.sleep(5)
        user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR, "._aj1- .x1nhvcw1")
        login_button.click()
        time.sleep(5)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, ".x1yc6y37")
        not_now_button.click()
        time.sleep(5)
        notification_button = self.driver.find_element(By.CSS_SELECTOR, "._a9_1")
        notification_button.click()


    def find_followers(self):
        self.driver.get(url=ACCOUNT_URL)
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, ".x1uw6ca5:nth-child(2) .x18hxmgj")
        followers.click()
        time.sleep(2)

    def follow(self):
        while True:
            try:
                list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'button')
                print(len(list_of_people))
                for person in list_of_people:
                    print(person.text)
                    if person.text == "Follow":
                        time.sleep(random.randint(1, 2))
                        self.driver.execute_script("arguments[0].click();", person)
                        time.sleep(random.randint(10, 15))
                    print(len(list_of_people))
                print("Scrolling...")

                fbody = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
                scroll = 0
                while scroll < 5:
                    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
                    time.sleep(2)
                    scroll += 1

            except Exception as e:
                print(e)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
time.sleep(3)
