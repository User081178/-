import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from faker import Faker


@pytest.fixture(autouse=True)
def browser():
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()


    yield driver
    driver.quit()