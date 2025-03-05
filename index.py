from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

def test_login():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")
    username.send_keys("student")
    password.send_keys("Password123")
    login_button.click()
    time.sleep(2)
    assert "Logged In Successfully" in driver.page_source, "Login failed!"
  

def test_form_validation():
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    time.sleep(2)
    email = driver.find_element(By.NAME, "fname")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    email.send_keys("invalid-email")
    submit_button.click()
    time.sleep(1)

def test_ui_elements():
    driver.get("https://practicetestautomation.com/")
    time.sleep(2)
    assert driver.find_element(By.LINK_TEXT, "Practice"), "Practice page link missing!"
    assert driver.find_element(By.LINK_TEXT, "Test Login Page"), "Login page link missing!"
    
test_login()
test_form_validation()
test_ui_elements()

driver.quit()



