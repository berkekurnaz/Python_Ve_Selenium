from selenium import webdriver
import time

browser = webdriver.Chrome()

url = "http://lezzetlisunumlarim.com/"

browser.get(url)

time.sleep(5)

browser.close()


