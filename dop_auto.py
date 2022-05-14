from selenium import webdriver
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from google.cloud import vision
import os
import csv
import io
import cv2

browser=webdriver.Chrome()
browser.maximize_window()

username='DOP.MIG0017258'
password='Jamuna@73123'
credential_path = "\\Users\\HP\\Downloads\\dopautom-9f2f1a082393.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

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
cropped_image = image[330:360, 1250:1400]
cv2.imwrite("Cropped Image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:{}'.format(texts[0].description))
    return texts[0].description

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

captcha=browser.find_element_by_id("AuthenticationFG.VERIFICATION_CODE")
captcha.send_keys(str(detect_text('\\Users\\HP\\Desktop\\Git Repo\\DOP Automation\\Cropped Image.jpg')).strip('\n'))
time.sleep(7)

browser.find_element_by_id('VALIDATE_RM_PLUS_CREDENTIALS_CATCHA_DISABLED').click()
time.sleep(3)

browser.find_element_by_id('Accounts').click()
browser.find_element_by_id('Agent Enquire & Update Screen').click()

row_len = len(browser.find_elements_by_xpath('/html/body/form/div[1]/div[4]/div[4]/div/div/div/div/div/div/div/table/tbody/tr'))
print(row_len)
col_len = len(browser.find_elements_by_xpath('/html/body/form/div[1]/div[4]/div[4]/div/div/div/div/div/div/div/table/tbody/tr'))
print(col_len)

accounts=[]
account_row=[]
for i in range(3,row_len):  
  for j in range(2,6):
    account_row.append(browser.find_element_by_xpath('/html/body/form/div[1]/div[4]/div[4]/div/div/div/div/div/div/div/table/tbody/tr['+str(i)+']/td['+str(j)+']').text)
    print(account_row)