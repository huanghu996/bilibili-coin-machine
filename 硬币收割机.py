import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test():
    driver = webdriver.Chrome("chromedriver.exe")  
    driver.get(r"https://passport.bilibili.com/login")
    driver.find_element_by_id("login-username").send_keys("你的账号")
    driver.find_element_by_id("login-passwd").send_keys("你的密码")
    driver.find_element_by_xpath('//a[@class="btn btn-login"]').click()

if __name__ == "__main__":
    test()
    os.system("pause")