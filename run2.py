import os
import time

from selenium.webdriver.chrome.webdriver import WebDriver

mail_address = 'rama_dhan18'
password = 'allahuakbar'

from selenium import webdriver

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'))  # Optional argument, if not specified will search path.

url = 'https://instagram.com'
driver.get(url)
time.sleep(2)

driver.find_element_by_class_name('_2hvTZ.pexuQ.zyHYP').send_keys(mail_address)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
time.sleep(2)
driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF").click()

url = 'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22CHs4E59loFy%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D'
driver.get(url)

# time.sleep(7)
# #driver.find_element_by_id("Passwd").send_keys(password)
#driver.find_element_by_id("signIn").click()