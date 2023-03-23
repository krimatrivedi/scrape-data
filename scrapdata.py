import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


WAIT_TIME = 10

# Here Chrome will be used
driver = webdriver.Chrome()

# URL of website

url="https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
    # Opening the website
driver.get(url)
#first link will be opened to exctract the data
linkofdata=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//a[starts-with(@onclick, 'prevnext')]")))
# click button
linkofdata.click()   
time.sleep(5)
#loop for number of links avaliable on page
for i in range(6):

        page_source = driver.page_source
        #pandas for scraping the data
        import pandas as pd
        dfs = pd.read_html(page_source)
        dfs1=dfs[4]
        dfs2=dfs[5]
        print(dfs1.iloc[[0,2]])
        if i<=2 or i==5:
            #rows are adjusted as it's different in some pages
            print(dfs2.iloc[1])
        else:
            print(dfs2.iloc[2],i)
        
        time.sleep(5)
        try:
            #look for next page
            nextpage=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "id_prevnext_next")))
            nextpage.click()
        except:
            print("error")


