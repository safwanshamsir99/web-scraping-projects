from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service

#keyword = input("Keyword:") #search keyword
#page = input("Page:") #how many pages to scrap
#filename= input("File name:") #output filename

#webdriver option
#opt = webdriver.EdgeOptions()
opt = webdriver.EdgeOptions()
#opt.add_argument('--no-sandbox') #Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only.
opt.add_argument('--headless') #Run in headless mode, i.e., without a UI or display server dependencies.
#opt.add_argument('--disable-notifications')#Disables the Web Notification and the Push APIs.

# edge_path = r"C:\Users\Acer\OneDrive\Documents\Work\INVOKE\shopee-web-scrape\msedgedriver.exe"
# service = Service(executable_path=edge_path)
service = Service('msedgedriver.exe')
driver = webdriver.Edge(service=service,options=opt) #setting up webdriver and option
path_link = 'https://shopee.com.my/search?keyword=macbook'
driver.get(path_link) #target website
time.sleep(5) #pauses to fully load the page and prevents the web from detecting us as a bot

driver.save_screeshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'html.parser')
print(data.encode("utf-8"))

#search
#search = driver.find_element(By.XPATH,'//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input') 
#search.send_keys(keyword) 
#search.send_keys(Keys.ENTER)
#time.sleep(5)

# zoom out
#driver.execute_script("document.body.style.zoom='10%'")
#time.sleep(2)

# blank var to contain the page data
#data=str()

# pagination
#for k in range (int(page)) :
    #fetch all the data on the page
    #data += driver.page_source
    #time.sleep(5)

    # navigate to the next page
    #next = driver.find_element(By.CSS_SELECTOR,' button.shopee-icon-button.shopee-icon-button--right ')
    #driver.execute_script("arguments[0].click();", next)
    #time.sleep(5)


# driver.close()

