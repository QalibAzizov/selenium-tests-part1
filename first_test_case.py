# 1) Open Web Browser (Chrome/firefox/Edge)
# 2) Open URl https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin)
# 4) Enter password (admin123)
# 5) Click on Login
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('/usr/local/bin/chromedriver')


driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(20)




driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()



act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")   
    






