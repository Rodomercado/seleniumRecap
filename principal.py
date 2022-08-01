from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.find_element('name', 'user-name').send_keys('standard_user')
driver.find_element('name','password').send_keys('secret_sauce')
driver.find_element('name','login-button').click()
time.sleep(5)
driver.quit()
