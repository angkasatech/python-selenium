import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


wait_time = 1000
email = 'sundhanz@gmail.com'
#driver = webdriver.Firefox(executable_path=os.path.abspath('geckodriver.exe'))  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'))  # Optional argument, if not specified will search path.
driver.get('https://youtu.be/h2sf-eVvAAw');
driver.find_element_by_id('text').click()
time.sleep(10)
driver.find_element_by_id('identifierId').send_keys(email)

"""
element = WebDriverWait(driver, wait_time).until(
    EC.presence_of_element_located((By.ID, "identifierNext"))
)
"""
driver.implicitly_wait(20)

driver.find_element_by_id('identifierNext').click()


"""
element = WebDriverWait(driver, wait_time.until(
    EC.element_to_be_clickable(By.Name, css)))
"""