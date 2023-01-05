from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 
url = "https://www.azquotes.com/quote/1221297"

path_to_extension = r"C:/Users/bozku/OneDrive/Masaüstü/5.2.0_0"
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

s=Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s,chrome_options=chrome_options)
browser.create_options()


browser.get(url)
time.sleep(10)
i = 0 
with open('Jean-Jacques Rousseau.txt', 'w') as f:
    while i <400 :
        text = browser.find_element(By.CLASS_NAME, "single-quote").text
    
        f.write(text)
        f.write("\n")
        print(text)
        time.sleep(1)
        next = browser.find_element(By.CLASS_NAME, "next")
        next.click()
        time.sleep(1)
        i+=1
    
    
#b = browser.find_element(By.CLASS_NAME, "single-quote").text
#print("aa",b)

