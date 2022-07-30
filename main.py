import re
from multiprocessing import Pool
from random import choice

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from multiprocessing.dummy import Pool

from time import sleep
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")


acc = 5 # сколько зарегать акков
o = ("1")
mail42 = o * acc


f = open('mail.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("mail.txt", "r") as f:
    private = f.read().split('\n')
    i = i - 1




def work(private):
    try:
        print(private)
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        driver.get('https://sdcc.cryptoys.com/cryptoys-masters-of-the-universe?utm_source=discord&utm_medium=social&utm_campaign=nft-gift')
        wait.until(EC.element_to_be_clickable((By.ID, 'email-471463cd-af39-4619-94e5-b0c60d4ccc3f_3401'))).send_keys(private)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="SUBSCRIBE"]'))).click()


        with open('valid.txt', 'a') as file:
            file.write(f'{private}\n')
            print(f'Зарегал {private}')

        time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=3) # кол-во потоков
    p.map(work, private)
