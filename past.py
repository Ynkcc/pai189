from selenium import webdriver
import time
import json
import datetime
import requests
import re
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
#option.add_argument('headless') #添加无头浏览
option.add_experimental_option("detach",True)
browser = webdriver.Chrome(options=option)
browser.implicitly_wait(10)
browser.set_window_size(800,1080)
browser.get('https://pai.189.cn/')
time.sleep(40)#登录时间

def hasVoucher(browser):
    browser.get('https://pai.189.cn/#/customer/myPage')
    time.sleep(1)
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div[1]/div[2]/div/div[4]/div[2]/div/div').click() #我的圈子
    
    Original_result=browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div[2]/span').text #圈子页面流量券  
    matchResult=re.match(r'还有(\d+)张流量券未领取', Original_result)
    if(matchResult):
        number=int(matchResult.group(1))
        if(number>0):
            return True
    return False
def retire(browser):
    #browser.get('https://pai.189.cn/#/customer/myPage')
    #browser.refresh()
    time.sleep(1)
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div[1]/div[2]/div/div[4]/div[2]/div/div').click() #我的圈子
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div/img[2]').click()  #设置
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div/div').click() #退出
    browser.find_element(By.XPATH,r'//*/div/div[2]/div/div/div[2]/div/a[2]').click() #退出确认
def join(browser,url):
    browser.get(url)
    browser.refresh()
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div/div[3]/div[2]/div[2]/div[1]')
    time.sleep(2)
    Original_result=browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div/div[3]/div[2]/div[2]/div[1]').text #邀请过期或时间
    if(Original_result.find("距离邀请失效还有")==-1):
        return False
    browser.find_element(By.XPATH,r'//*[@id="root"]/div/div[4]/div/div/div[3]/div[2]/div[2]/a').click() #加入
    time.sleep(1)
    browser.find_element(By.XPATH,r'//*/div/div[2]/div/div/div[3]/div/a[2]').click() #加入确认

for marketingCircleInstId in range(11016,12000):
    if marketingCircleInstId%21==0:
        print(marketingCircleInstId)
    url='https://pai.189.cn/#/sect/martailInvite?marketingCircleInstId='+str(marketingCircleInstId)
    if(join(browser,url)==False):
        continue
    if(hasVoucher(browser)):
        print("ok "+marketingCircleInstId)
    retire(browser)

