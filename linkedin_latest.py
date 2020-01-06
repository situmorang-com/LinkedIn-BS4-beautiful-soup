import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument('headless')  //Uncomment it to get the headless mode
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=options,executable_path=r"/home/rohit/web_crawling/chromedriver")
#change the driver path according to your local machine where you kept it.


driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

driver.maximize_window()

time.sleep(2)
#source.clear()

email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys('instagramthelastpage@gmail.com')

email.send_keys('')
time.sleep(1)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Jack@123')

password.send_keys('')
time.sleep(1)

submit = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
submit.click()
time.sleep(2)

driver.get('https://www.linkedin.com/in/situmorang')



html=driver.page_source

soup=bs(html,"lxml")
ext=soup.find(class_='flex-1 mr5')

fp=open("edmund.csv","w")

x_li=ext.find_all('li')
for x in x_li:
    fp.write(x.getText())

fp.close()
driver.quit()
