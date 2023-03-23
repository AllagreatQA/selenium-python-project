import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium_practice.example_6 import options

ptions = webdriver.ChromeOptions()
options.add_argument("--headless=new")
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('http://ec2-35-77-8-202.ap-northeast-1.compute.amazonaws.com/')
print(browser.title)
time.sleep(2)