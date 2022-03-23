import requests
import datetime
import random
import platform
import random
import string
import subprocess
import undetected_chromedriver as uc
import sys
import requests
import names
import csv
import zipfile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import randint, randrange
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from random import choice
from fake_headers import Headers
from selenium.common.exceptions import TimeoutException
from plugin_config import background_js, manifest_json

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

now = datetime.datetime.now().time()

def type_me(element, text):
    for letter in text:
        element.send_keys(letter)

def type_number(element, number):
    element.send_keys(number)

def print_message(msg):
    print(f'{msg}')

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

print_message('\033[35m'+ """     _                             _              ____                           _             
    / \   ___ ___ ___  _   _ _ __ | |_           / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / _ \ / __/ __/ _ \| | | | '_ \| __|  _____  | |  _ / _ | '_ \ / _ | '__/ _` | __/ _ \| '__|  
  / ___ | (_| (_| (_) | |_| | | | | |_  |_____| | |_| |  __| | | |  __| | | (_| | || (_) | |   
 /_/   \_\___\___\___/ \__,_|_| |_|\__|          \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                  
""" + '\033[0m')

print_message(f'\033[34m [{datetime.datetime.now().time()}] Starting Account Generator v1.3 2022...\033[0m  \n')

OSNAME = platform.system()

if OSNAME == 'Linux':
    OSNAME = 'lin'
    with subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE) as proc:
        version = proc.stdout.read().decode('utf-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Darwin':
    OSNAME = 'mac'
    process = subprocess.Popen(
        ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
    version = process.communicate()[0].decode(
        'UTF-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Windows':
    OSNAME = 'win'
    process = subprocess.Popen(
        ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
    )
    version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
else:
    print('{} OS is not supported.'.format(OSNAME))
    sys.exit()

major_version = version.split('.')[0]

uc.TARGET_VERSION = major_version

# Random Name - Number

n = random.randint(0,20000)
day_random = randrange(27)
month_random = randrange(12)
year_random = random.randint(1980,2000)
list = open("proxies.txt", "r").readlines()

def get_session(country,firstName,lastName,email_Input,password_Input,num_account):
    for i in range(0, num_account):
        try:
            proxy = random.choice(list).rstrip()
            proxy_split = proxy.split(":")
            PROXY_HOST = proxy_split[0]
            PROXY_PORT = proxy_split[1]
            PROXY_USER = proxy_split[2]
            PROXY_PASS = proxy_split[3]

            header = Headers(
            browser="chrome",
            os=OSNAME,
            headers=False
            ).generate()
            agent = header['User-Agent']
        
            options = webdriver.ChromeOptions()
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js %
                            (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))
            options.add_extension(pluginfile)

            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option('prefs', {
                'credentials_enable_service': False,
                'profile': {
                    'password_manager_enabled': False
                }
            })
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--disable-web-security")
            viewport = ['2560,1440', '1920,1080']
            options.add_argument(f"--window-size={choice(viewport)}")
            options.add_argument("--log-level=3")
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument(f"user-agent={agent}")
                      
            s=Service('/Users/admin/webdrivers/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            wait = WebDriverWait(browser, 3)

            print(' ')
            print(f'\033[92m [{datetime.datetime.now().time()}] Getting Session ...\033[0m')
            print(f'\033[92m [{datetime.datetime.now().time()}] Filling DATA ...\033[0m')
            print(f'\033[92m [{datetime.datetime.now().time()}] Proxy: {proxy} \033[0m')

            url = f'https://www.yoox.com/{country}/myoox/register?'
            browser.get(url)
            
            # First and Last name pick
            if firstName != "RANDOM":
                first = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Name"]')))
                type_me(first, firstName)
            else:
                first = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Name"]')))
                type_me(first, names.get_first_name())

            if lastName != "RANDOM":
                last = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SurName"]')))
                type_me(last, lastName)
            else:
                last = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SurName"]')))
                type_me(last, names.get_last_name())
            
            # Email and Password pick
            random_email = random_char(15) + email_Input
            email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Email"]')))
            type_me(email, random_email)

            password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
            type_me(password, password_Input)

            # Date pick     
            day = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Day"]')))
            type_number(day, day_random)
            
            month = wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="Month"]')))
            type_number(month, month_random)
        
            year = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Year"]')))
            type_number(year, year_random)

            # phone Number pick
            phone_Number = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PartialMobilePhone"]')))
            type_number(phone_Number, random_with_N_digits(10))
        
            # Button
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[2]/div[2]/button[1]'))).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[3]/div/form/input[7]'))).click()
    
            # Check Account 
            try:
                wait.until(EC.url_to_be("https://www.yoox.com/myoox?newFb=False"))
                print(f'\033[34m [{datetime.datetime.now().time()}] ACCOUNT GENERATE ! \033[0m')
                csvData = [[random_email,password_Input]]
                with open('accounts.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
            except TimeoutException:
                print(f'\033[31m [{datetime.datetime.now().time()}] Rotating headers... \033[0m')
                pass
                        
        except requests.exceptions.Timeout:
            print(f'\033[31m [{datetime.datetime.now().time()}] An error occurred --> change proxies \033[0m')

# Request with Session

if __name__ == '__main__':
    s = requests.Session()
    country = input(f'\033[36m [{datetime.datetime.now().time()}] 1. Insert Your Country [must contain only 2 digits] IT --> Italy: \033[0m')
    firstName = input(f'\033[36m [{datetime.datetime.now().time()}] 2. Insert Your Name... RANDOM --> RANDOM: \033[0m')
    lastName = input(f'\033[36m [{datetime.datetime.now().time()}] 3. Insert Your Last Name... RANDOM --> RANDOM: \033[0m')
    email_Input = input(f'\033[36m [{datetime.datetime.now().time()}] 4. Insert Your Catchall --> @catchall.com: \033[0m')
    password_Input = input(f'\033[36m [{datetime.datetime.now().time()}] 5. Insert Your Password... --> AT LEAST 8 CHARACTERS AND ONE NUMBER: \033[0m')
    num_account = int(input(f'\033[36m [{datetime.datetime.now().time()}] 6. How Many Account ? --> 10: \033[0m'))

    get_session(country,firstName,lastName,email_Input,password_Input,num_account)

#- TO DO LIST -#

# check ip during the resgistration
# Implementation CLI.exe

# -- Maybe -- #

# Add run more task in the same time
