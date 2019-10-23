from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
string = ''
# ______________________________________

# Opening thetypingcat.com on firefox
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
firefox = webdriver.Firefox(capabilities=cap)
firefox.get('https://www.nitrotype.com/login')

firefox.find_element_by_css_selector("#username").send_keys("FatFingersFred")
firefox.find_element_by_css_selector("#password").send_keys("fatfingersfredpassowrd")

# ______________________________________

# Using javascript to get the typing content from the website and storing value in "string" variable

for i in range(firefox.execute_script('return document.querySelectorAll(".dash-letter").length')):
	string += firefox.execute_script('return document.querySelectorAll(".dash-letter")['+str(i)+'].innerHTML')

string = re.sub(r'<[^>]*>','',string) #This line is just delete tags present inside string
print(string)
# ______________________________________

# Selenium commands to type what is stored inside string variable on the focused screen

action = ActionChains(firefox)
action.send_keys(string)
action.perform()