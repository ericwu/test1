from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--disable-notifications")
s = Service(r"./chromedriver.exe")

chrome = webdriver.Chrome(service=s, options=options)

chrome.get("https://www.google.com")