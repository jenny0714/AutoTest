from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ("/home/jenny/Tool/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://cyan92128505.github.io/gliona/#/login")
search = driver.find_element_by_name("username")
search.clear()
search.send_keys("test@gliona.com")
search = driver.find_element_by_name("password")
search.send_keys("test1234")
search.send_keys(Keys.RETURN)

# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.LINK_TEXT,"歡迎使用GLIONA"))
# )
time.sleep(5)

link = driver.find_element_by_link_text("點擊這裡開始管理你拜訪的獸醫院")
link.click()
time.sleep(5)

titles = driver.find_elements_by_class_name("MuiButtonBase-root")
for title in titles:
    print(title.text)
driver.back()

time.sleep(5)


print(driver.title)
driver.quit()

