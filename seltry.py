from re import search
import webbrowser
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
url= "https://aemo.com.au/en/energy-systems/electricity/national-electricity-market-nem/data-nem/data-dashboard-nem"
driver.maximize_window()
driver.get(url)

button = driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div/div/div/div/div/ul/li[2]/div/div/div/div")
button.click()
