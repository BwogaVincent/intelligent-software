#Task1 AI-powered code completion
def sort_dict_list(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])

# Manual Implementation

def sort_dict_list(dict_list, key):
    for i in range(len(dict_list)):
        min_idx = i
        for j in range(i+1, len(dict_list)):
            if dict_list[j][key] < dict_list[min_idx][key]:
                min_idx = j
        dict_list[i], dict_list[min_idx] = dict_list[min_idx], dict_list[i]
    return dict_list



#Task2 Automated Testing with AI
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login(username, password, expected_result):
    driver = webdriver.Chrome()
    driver.get("https://malaria-outbreak-platform.example/login")
    
    # AI-generated element locators
    username_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    submit_button = driver.find_element(By.ID, "login-btn")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    time.sleep(2)
    
    if expected_result == "success":
        assert "dashboard" in driver.current_url
    else:
        error_message = driver.find_element(By.CLASS_NAME, "error-message")
        assert "Invalid credentials" in error_message.text
    
    driver.quit()

# Test cases
test_login("valid_user", "correct_password", "success")
test_login("invalid_user", "wrong_password", "failure")
