from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/Users/areyoureddy/Web Development/Development Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Rent Hop is the NYC Real Estate website for renters and buyers.
driver.get("https://www.renthop.com/")

#Filtering the data based off of the requirements of the users of the data
bedrooms = driver.find_element(By.XPATH, '//*[@id="home-beds-container"]/div/div[3]/label/div').click()
time.sleep(5)
search_bar = driver.find_element(By.XPATH, '//*[@id="area-text"]')
search_bar.click()
time.sleep(5)
no_ho = driver.find_element(By.XPATH, '//*[@id="group-tab-downtown-manhattan-new-york-ny"]/div[10]/label/div[1]')
no_ho.click()
time.sleep(2)
scrollable_popup = driver.find_element(By.XPATH, '//*[@id="search-nyc-body"]')

#This is the scrolling feature - it will scroll 5 times
scroll = 0
while scroll < 3: 
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scrollable_popup)
    time.sleep(5)
    scroll += 1

midtown = driver.find_element(By.XPATH, '//*[@id="area-tab-manhattan-new-york-ny"]/div[4]/label/div[1]').click()
time.sleep(5)
x = driver.find_element(By.XPATH, '//*[@id="area-autocomplete-modal"]/div[2]/div').click()
time.sleep(5)

#Move to the next page to filter by the max rent
max_rent = driver.find_element(By.XPATH, '//*[@id="max-price"]')
max_rent.click()
time.sleep(5)
for x in range(5):
    max_rent.send_keys(Keys.BACKSPACE)
    time.sleep(2)
#Input my max rent in the search bar
max_rent.send_keys("5000")
time.sleep(5)
search_bar2 = driver.find_element(By.XPATH, '//*[@id="all-filters"]/div[3]/div[6]/div/div/div[1]/div/span').click()
time.sleep(8)

#Grabbed this snippet of code from the Medium article: Scraping Amazon results with Selenium and Python
try:
    number_page = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[5]/span/span[2]')
except NoSuchElementException:
    number_page = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[5]/a[2]').click()
time.sleep(5)

url_list = []

for i in range(int(number_page.text)):
    page_num = i + 1
    url_list.append(driver.current_url)
    time.sleep(4)
    next_page_num = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[5]/a[2]').click()                  
    print("Page " + str(page_num) + " was grabbed")


with open('search_results_urls.txt', 'w') as filehandle:
        for result_page in url_list:
            filehandle.write('%s\n' % result_page)
print("---DONE---")

for x in url_list:
    rental_information = driver.find_element_by_xpath('//*[@id="search-results-list"]')
    price_content = rental_information.get_attribute('innerHTML').strip()
    text = driver.find_element_by_xpath('//*[@id="search-results-list"]').text
    print(text)


driver.quit()