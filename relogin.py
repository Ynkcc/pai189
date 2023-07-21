from selenium import webdriver
import time
import json

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
listCookies=json.load(open('storeCookie.json','r',encoding='utf-8'))
#option.add_argument('headless') #添加无头浏览
browser = webdriver.Chrome(options=option)
browser.get('https://pai.189.cn/')
time.sleep(2)
browser.delete_all_cookies() 
for cookies in listCookies:
    browser.add_cookie(cookies)
browser.refresh()

#browser.close()
