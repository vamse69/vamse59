password = "Vamse@59n"
email = 'vamse69@gmail.com'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time
import os

repasitarynameinput = input("Enter Repasitary Name: ")

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://github.com/login')
time.sleep(5)
user = driver.find_element_by_id('login_field')
user.send_keys(email)

user = driver.find_element_by_id('password')
user.send_keys(password)

time.sleep(6)
signid = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]')
signid.submit()

time.sleep(6)
new = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a')
new.click()
time.sleep(5)
repasitaryname = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')

repasitaryname.send_keys(repasitarynameinput)
time.sleep(5)
redmeclick = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]')
redmeclick.click()
time.sleep(5)
crepasitary = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
crepasitary.submit()

time.sleep(5)
codeclick = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div/div/div[2]/div[1]/div[2]/span/get-repo/details/summary')
codeclick.click()

crepasitarypath = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/tab-container/div[2]/div/div/clipboard-copy')
crepasitarypath.click()

giturl = clipboard.paste()



'''
os.system('git config --global user.name'+email)
os.system('git config --global user.name "vamse69"')
'''

os.system('git init')

os.system('git add .')
os.system('git status')
os.system('git config --global user.email'+email)
os.system('git commit -m "Initial commit"')
os.system('git remote add origin '+giturl)
os.system('git push -f origin master')




print("\n Task Completed")