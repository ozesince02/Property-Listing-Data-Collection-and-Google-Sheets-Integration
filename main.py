import time
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

GOOGLE_SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd9GBiMpNEz4Z6ZMWaxNhNCdODe5fHAclVF9v9w8-cx8Zg40A/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.88159201281336%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.66883883415068%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A389711%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")

chrome_driver_path = "C:\dev\chromedriver.exe"
service = Service(chrome_driver_path)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "*/*",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

request = requests.get(url=ZILLOW_LINK, headers=HEADERS)
soup = BeautifulSoup(request.text, 'html.parser')

information = soup.find('script', {"data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip("<!--").strip("-->")
information_dict = json.loads(information)
house_result_dict = information_dict['cat1']['searchResults']['listResults']

all_prices = []
all_urls = []
all_addresses = []

for listing in house_result_dict:
    url = listing['detailUrl']
    if "http" not in url:
        all_urls.append(f"https://www.zillow.com{url}")
    else:
        all_urls.append(url)
    address = listing['address']
    try:
        price = listing['price']
    except KeyError:
        price = listing['units'][0]['price']

    all_addresses.append(address)
    all_prices.append(price)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(GOOGLE_SHEET_URL)

for i in range(len(all_urls)):
    time.sleep(3)
    address_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(all_addresses[i])
    price_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.send_keys(all_prices[i])
    link_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(all_urls[i])
    submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    time.sleep(1)
    submit.click()
    time.sleep(1)
    if i < len(all_urls)-1:
        submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another.click()

driver.quit()
