from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Input username and password in following variables
username = ''
password = ''

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website and wait for the webpage to load
driver.get('https://apexfusion.com/login')

#try:
#  id_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'index-login-username')))
#except NoSuchElementException:
#  #email message

# Enter username and password to login
id_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'index-login-username')))
id_box.send_keys(username)
pass_box = driver.find_element_by_id('index-login-password')
pass_box.send_keys(password)
login_button = driver.find_element_by_class_name('btn-primary').click()

#try:
#  id_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'index-login-username')))
#except NoSuchElementException:
#  #email message

# Find and click into Configuration menu
serial_filter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'af-toggle-down')))
serial_filter_button.click()
serial_filter_box = driver.find_element_by_id('list-filter-serial')
serial_filter_box.send_keys('57396')
serial_filter_box.send_keys(Keys.RETURN)
driver.implicitly_wait(3)
config_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'i.af-exclamation')))
config_dropdown.click()
config_summ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.list-summary')))
config_summ.click()
lab_dropdown = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'nav-main-menu-name')))
lab_dropdown.click()
