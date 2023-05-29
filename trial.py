import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(executable_path="C:\Automation\chromedriver_win32\chromedriver.exe",options= chrome_options)

driver = webdriver.Chrome(executable_path="C:\Automation\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@time='ten']")
driver.find_element(By.CSS_SELECTOR, "input[time='ten']")  #  .classname, #id

dropdown
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID,'dropdown-class-example')) # static drop down must need 'SELECT' tag
select.select_by_index(2)
select.select_by_visible_text("Option1")
select.select_by_value("attribute's vslue") # for this we need value attribute in html

# for dynamic dropdown we use for loop (with break statement) and compare with our selection then click on the element


#Checkbox
# checkbox = driver.find_element(By.ID,"checkBoxOption1")
# checkbox.click()
# print(checkbox.is_selected())
#
#
# #Radio button
# radio = driver.find_element(By.XPATH, "//input[@value='radio1']")
# radio.click()
# print(radio.is_displayed())
#
#
# #Javascript confirmation popup
# driver.find_element(By.ID, "alertbtn").click()
# alert= driver.switch_to.alert
# alert.accept()

# #confirmation popup
# driver.find_element(By.ID, "confirmbtn").click()
# alert= driver.switch_to.alert
# text = alert.text
# print(text)
# alert.dismiss()

# #mouse action
# from selenium.webdriver.common.action_chains import ActionChains
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.move_to_element(driver.find_element(By.ID, "mousehover")).click().perform()
# action.drag_and_drop("source,  target").perform()
# action.double_click("element").perform()
# action.context_click("element").perform()

#child window
# driver.switch_to.window(1)
# driver.switch_to.frame("iframe-name") # iframe must contain "iframe" tag
# driver.find_element(By.LINK_TEXT,"Learning Paths").click()
# driver.switch_to.default_content()
# driver.window_handles

# #scroll
# driver.execute_script("window.scrollBy(0,500)")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#screeenshot
# driver.save_screenshot("screen.png")

headlessmode
from selenium.webdriver.chrome.options import Options

chrome_options =  webdriver.ChromeOptions()

chrome_options.add_argument("headless")
driver = webdriver.Chrome(executable_path=" chromedriver.exe",options= chrome_options)


print("Pooja")
print("vsrfcs")

print("vsrfcs")
print("vsrfcs")
print("vsrfcs")

print("Pooja")
print("vsrfcs")

print("vsrfcs")
print("vsrfcs")
print("vsrfcs")

print("vsrfcs")
print("vsrfcs")
time.sleep(5)