from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"E:\Games\replays\pvp",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled" : True
})
driver = webdriver.Chrome(options=chrome_options)

for i in range(1, 251):
    driver.get(f'https://lotv.spawningtool.com/replays/?p=&pro_only&tag=9&p={i}')

    time.sleep(5)

    download_button = driver.find_element(By.CLASS_NAME, 'download-replays')
    download_button.click()
    time.sleep(1)
        

driver.quit()