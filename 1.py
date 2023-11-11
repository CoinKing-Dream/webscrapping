
# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import Actions
from selenium.webdriver.support import expected_conditions as EC
 
# create webdriver object
browser = webdriver.Chrome()
# browser.maximize_window()

# get google.co.in
browser.get("https://beds24.com/control2.php?pagetype=login")

# loading duration
sleep(2)

# login process
# userName = browser.find_elements(By.XPATH, '//*[@name="username"]')
# userName[0].send_keys("info@okiresort.com")

userName = browser.find_element(By.NAME, "username")
userName.send_keys("info@okiresort.com")

passWord = browser.find_elements(By.XPATH, '//*[@name="loginpass"]')
passWord[0].send_keys("Airb@Okinawa987")

# sleep(1)

loginBtn = browser.find_elements(By.XPATH, '//*[@name="dosubmit"]')
loginBtn[0].click()

# userName.clear()
# passWord[0].clear()

print("Successfully logined!")
sleep(1)

# setting report
# popselectBtn = browser.find_element(By.ID, "propselector")
# popselectBtn.click()

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="propselector"]/option[1]'))).click()

date_picker = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fshowfrom"]')))
date_picker.send_keys("2023-01-23")

# sleep(1)
dateFrom = browser.find_element(By.NAME, "fshowfrom")
dateFrom.send_keys("werwer")

# dateFrom = browser.find_element(By.ID, "fshowtil")
# dateFrom.click()
# sleep(1)

roomoccupancyBtn = browser.find_element(By.NAME, "roomoccupancy")
roomoccupancyBtn.click()

# reportBtn = browser.find_elements(By.XPATH, '//*[@id="thetopmenureports"]/div/div/a[1]')
# reportBtn[0].click()
sleep(2)

roomstateTable = browser.find_elements(By.XPATH, '//tbody/tr[1]/*')
# roomstateElement = browser.find_elements(By.XPATH, '//*table/tbody/tr[4]')
print(roomstateTable[0].text)
print(roomstateTable[1].text)
print(roomstateTable[2].text)
# for x in roomstateDate:
#     print(x.text)

sleep(5)
# print(element)
browser.quit()