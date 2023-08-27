import time
import pytest
from selenium import webdriver
from faker import Faker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver
    driver.quit()