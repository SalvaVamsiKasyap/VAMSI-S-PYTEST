import pytest
from time import sleep
import requests
from _pytest.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService



def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome")


@pytest.fixture(scope="class")

def setup(request):
    """This is used to do cross browser testing at run time"""
    browser_Name = request.config.getoption("browser_Name")
    response = requests.head("https://itero.com/en-APAC")
    response = str(response)[11:14]
    if browser_Name == "chrome" and response == '200':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_Name == "firefox" and response == '200':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_Name == "edge" and response == '200':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("https://itero.com/en-APAC")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

