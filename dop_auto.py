from selenium import webdriver
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import cv2

browser=webdriver.Chrome()
browser.maximize_window()

username='DOP.MIG0017258'
password='Smatheswaran@73'

total = 10
with open ('\\Users\\HP\\Desktop\\Git Repo\\DOP Automation\\accounts.txt','r') as file:
  list = file.readlines()

mul_list = []
for i in list:
  if '(' in i:
    mul_list.append(i)
	
print(mul_list)

acc = ''  
for i in list:
  acc = acc + i +','

acc = acc[:-1]
acc_ass ={}
with open('\\Users\\HP\\Desktop\\Git Repo\\DOP Automation\\account_asslass.csv','r') as csv_file:
  for row in csv_file:
    li = row.split(',')
    account = li[0].replace('\n','')
    asslass = li[1].replace('\n','')
    acc_ass[account] = str(asslass)
	
print(acc_ass)
wait=WebDriverWait(browser, 20);

browser.get("https://dopagent.indiapost.gov.in/")
time.sleep(2)
uname=browser.find_element_by_id("AuthenticationFG.USER_PRINCIPAL")
uname.send_keys(username)
time.sleep(2)

pwd=browser.find_element_by_id("AuthenticationFG.ACCESS_CODE")
pwd.send_keys(password)
time.sleep(2)

browser.save_screenshot('screenshot.png')
image = cv2.imread('screenshot.png')
cropped_image = image[310:340, 1250:1400]
cv2.imwrite("Cropped Image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

browser.find_element_by_id('VALIDATE_RM_PLUS_CREDENTIALS_CATCHA_DISABLED').click()
time.sleep(3)

browser.find_element_by_id('Accounts').click()
browser.find_element_by_id('Agent Enquire & Update Screen').click()

browser.find_element_by_xpath('/html/body/form/div[1]/div[4]/div[3]/p[3]/span/span[2]/textarea').send_keys(acc)

browser.find_element_by_id('Button3087042').click()

if total <=10:
  clickable = ''
  for i in range(0,total):
    clickable = 'CustomAgentRDAccountFG.SELECT_INDEX_ARRAY['+str(i)+']'
    browser.find_element_by_id(clickable).click()
    time.sleep(2)
else:
  clickable = ''
  for i in range(0,10):
    clickable = 'CustomAgentRDAccountFG.SELECT_INDEX_ARRAY['+str(i)+']'
    browser.find_element_by_id(clickable).click()
  browser.find_element_by_id('Action.AgentRDActSummaryAllListing.GOTO_NEXT__').click()
  for i in range (10,total):
    clickable = 'CustomAgentRDAccountFG.SELECT_INDEX_ARRAY['+str(i)+']'
    browser.find_element_by_id(clickable).click()
  
browser.find_element_by_id('CustomAgentRDAccountFG.PAY_MODE_SELECTED_FOR_TRN').click()
  
browser.find_element_by_id('Button26553257').click()

if total <= 10:
  acc_1 = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY[0]').text)
  browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc_1]))
  browser.find_element_by_id('Button11874602').click()
  time.sleep(1)
  for i in range(0,total-1):
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/form/div[1]/div[4]/div[5]/div/div/div/div/div/div/div/table/tbody/tr'+'['+str(4+i)+']'+'/td[1]/input').click()
    acc = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY['+str(i+1)+']').text)
    browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc]))
    time.sleep(1)
    browser.find_element_by_id('Button11874602').click()
	
else:
  acc_1 = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY[0]').text)
  browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc_1]))
  browser.find_element_by_id('Button11874602').click()
  time.sleep(1)
  for i in range(0,9):
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/form/div[1]/div[4]/div[5]/div/div/div/div/div/div/div/table/tbody/tr'+'['+str(4+i)+']'+'/td[1]/input').click()
    acc = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY['+str(i+1)+']').text)
    browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc]))
    time.sleep(1)
    browser.find_element_by_id('Button11874602').click()
  browser.find_element_by_id('Action.SelectedAgentRDActSummaryListing.GOTO_NEXT__').click()
  browser.find_element_by_id('CustomAgentRDAccountFG.SELECTED_INDEX').click()
  acc = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY[10]').text)
  browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc]))
  browser.find_element_by_id('Button11874602').click()
  for i in range(11,total):
    time.sleep(1)
    browser.find_element_by_id('Action.SelectedAgentRDActSummaryListing.GOTO_NEXT__').click()
    browser.find_element_by_xpath('//*[@value='+str(i)+']').click()
    acc = str(browser.find_element_by_id('HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY['+str(i)+']').text)
    browser.find_element_by_id('CustomAgentRDAccountFG.ASLAAS_NO').send_keys(str(acc_ass[acc]))
    time.sleep(1)
    browser.find_element_by_id('Button11874602').click()

browser.find_element_by_id('PAY_ALL_SAVED_INSTALLMENTS').click()

# /html/body/form/div[1]/div[4]/div[4]/div/div/div/div/div/div/div/table/tbody/tr[3]/td[1]/input
# HREF_CustomAgentRDAccountFG.ACCOUNT_NUMBER_ARRAY[10]//*[@id="CustomAgentRDAccountFG.SELECTED_INDEX"]


