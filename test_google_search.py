import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_solution():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("Selenium with Python")
    driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
    search_links = driver.find_elements(By.XPATH, "//h3[@class='LC20lb DKV0Md']")
    link = search_links[5]
    # driver.execute_script("arguments[0].scrollIntoView();", link)  # scroll down to the element
    # driver.execute_script("arguments[0].style.border='2px solid red';", link)
    # wait.until(EC.element_to_be_clickable(link))
    link.click()
    assert "Selenium with Python" in driver.page_source, "Given search text is present in the website."
    driver.quit()
