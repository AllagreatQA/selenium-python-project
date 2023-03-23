import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.google.com/')
print(browser.title)
time.sleep(2)
browser.refresh()
print(browser.title)
time.sleep(2)
browser.get('https://www.yahoo.com/')
print(browser.title)
time.sleep(2)
browser.back()
time.sleep(2)
print(browser.title)
browser.forward()
print(browser.title)
time.sleep(2)






