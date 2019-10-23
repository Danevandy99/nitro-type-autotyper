from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import time
import random
string = ''
# ______________________________________

# Opening thetypingcat.com on firefox
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
firefox = webdriver.Firefox(capabilities=cap)
firefox.get('https://www.nitrotype.com/login')

firefox.find_element_by_css_selector("#username").send_keys("TentacleTom")
time.sleep(1 * random.random())
firefox.find_element_by_css_selector("#password").send_keys("TTTT")
time.sleep(1 * random.random())
firefox.find_element_by_css_selector("[type=submit]").click()
time.sleep(1 * random.random())
firefox.get('https://www.nitrotype.com/race')


# ______________________________________

# Using javascript to get the typing content from the website and storing value in "string" variable
while len(firefox.find_elements_by_css_selector(".dash-letter")) < 1:
	time.sleep(0.1)

letters = firefox.find_elements_by_css_selector(".dash-letter")

for i in range(len(letters)):
	string += letters[i].get_attribute("innerHTML")

string = re.sub(r'<[^>]*>','',string) #This line is just delete tags present inside string
string = string.replace("&nbsp;", " ")
print(string)
# ______________________________________

# Selenium commands to type what is stored inside string variable on the focused screen

action = ActionChains(firefox)
action.send_keys(string)
action.perform()