import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Resource_tracker():
    def __init__(self):
        self.metal = 0
        self.crystal = 0
        self.deuterium = 0
        self.energy = 0
        self.hourly_metal = 0
        self.hourly_crystal = 0
        self.hourly_deuterium = 0
        self.maximum_metal = 0
        self.maximum_crystal = 0
        self.maximum_deuterium = 0
        self.energy_total = 0
        self.energy_used = 0

    def update_resources(self):
        self.metal = driver.find_element_by_xpath('//*[@id="resources_metal"]').text
        self.crystal = driver.find_element_by_xpath('//*[@id="resources_crystal"]').text
        self.deuterium = driver.find_element_by_xpath('//*[@id="resources_deuterium"]').text
        self.energy = driver.find_element_by_xpath('//*[@id="resources_energy"]').text
        #self.hourly_metal = driver.find_element_by_xpath('//*[@id="messages"]/div[12]/div[3]/div/div/table/tbody/tr[3]/td/span').text
        self.hourly_metal = driver.find_element_by_css_selector('#overview > div:nth-child(17) > div.t_Content > div > div > table > tbody > tr:nth-child(2) > td > span').text
        self.hourly_crystal = driver.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[16]/td[3]/span').text
        self.hourly_deuterium = driver.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[16]/td[4]/span').text
        self.maximum_metal = driver.find_element_by_xpath('//*[@id="messages"]/div[12]/div[3]/div/div/table/tbody/tr[2]/td/span').text
        self.maximum_crystal = driver.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[15]/td[3]/span').text
        self.maximum_deuterium = driver.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[15]/td[4]/span').text
        self.energy_total = driver.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[7]/td[6]/span').text
        self.energy_used = (self.energy_total - self.energy)



    def get_metal(self):
        return self.metal

    def get_crystal(self):
        return self.crystal

    def get_deuterium(self):
        return self.deuterium

    def get_energy(self):
        return self.energy

    def get_total_resources(self):
        return  (self.metal + self.crystal + self.deuterium)

    def get_hourly_metal(self):
        return self.hourly_metal

    def get_hourly_crystal(self):
        return self.hourly_crystal

    def get_hourly_deuterium(self):
        return self.hourly_deuterium

    def get_maximum_metal(self):
        return self.maximum_metal

    def get_maximum_crystal(self):
        return self.maximum_crystal

    def get_maximum_deuterium(self):
        return self.maximum_deuterium

    def get_energy_total(self):
        return self.energy_total

    def get_energy_used(self):
        return self.energy_used





CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
CHROMEDRIVER_PATH = 'D:\\03Programs\\Python-Geckodriver\\chromedriver.exe'

WINDOW_SIZE = "1920, 1080"
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options = chrome_options)

'''
Have a file called 'login.txt' in the same directory
It has to have the following entries:
user = YOURUSER
pass = YOURPASSWORD
univ = YOURSERVER
'''
with open('login.txt', 'r') as login_file:
    lines = []
    for line in login_file:
        lines.append(line)
    usr = str(lines[0]).split('=')[1].strip()
    pwd = str(lines[1]).split('=')[1].strip()
    srv = str(lines[2]).split('=')[1].strip()
    login_file.close()

driver.get('https://en.ogame.gameforge.com/')
driver.maximize_window()

#sleep(3)
#driver.find_element_by_id('MAX_0278f4c4').__setattr__('visibility', 'hidden')
#driver.switch_to.frame('https://static.crm.gfsrv.net/banner/TERA/171212_EventServer/550x480/550x480.html')
#sleep(1)

#wait = WebDriverWait(driver, 5)
#wait.until(EC.presence_of_element_located((By.ID, "openX_int_closeButton")))
#wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "openX_int_closeButton")))
#print('bla')

#adclose_button = driver.find_element_by_class_name('openX_int_closeButton')
#adclose_button.click()

sleep(1)
login_button = driver.find_element_by_id('loginBtn')
login_button.click()

usr_box = driver.find_element_by_id('usernameLogin')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_id('passwordLogin')
pwd_box.send_keys(pwd)

srv_box = driver.find_element_by_id('serverLogin')
srv_box.send_keys(srv)

submit_button = driver.find_element_by_id('loginSubmit')
submit_button.submit()

#works
#defense_button = driver.find_element_by_xpath('//*[@id="menuTable"]/li[7]/a/span')
#defense_button.click()

resources = Resource_tracker()
resources.update_resources()

print('Metal: %s\nCrystal: %s\nDeuterium: %s\nEnergy: %s\nHourly Metal: %s\nHourly Crystal: %s\nHourly Deuterium: %s'
      'Maximum Metal: %s\nMaximum Crystal: %s\nMaximum Deuterium: %s\nEnergy Total: %s\nEnergy Used: %s' % \
      (resources.get_metal(), resources.get_crystal(), resources.get_deuterium(), resources.get_energy(),
       resources.get_hourly_metal(), resources.get_hourly_crystal(), resources.get_hourly_deuterium(),
       resources.get_maximum_metal(), resources.get_maximum_crystal(), resources.get_maximum_deuterium(),
       resources.get_energy_total(), resources.get_energy_used()))