from selenium import webdriver

website = 'https://shopee.com.my/Shirt-col.3850164'
#path = 'C:\Users\Acer\Downloads\msedgedriver'
driver = webdriver.Edge()
driver.get(website)

driver.quit()
