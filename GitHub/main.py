from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/Users/areyoureddy/Web Development/Development Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Rent Hop is the NYC Real Estate website for renters and buyers.
driver.get("https://www.renthop.com/")