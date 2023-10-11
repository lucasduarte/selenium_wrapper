import os
from dotenv import load_dotenv

import undetected_chromedriver as uc

import time

class SeleniumWrapper:
    
    load_dotenv()
    
    WAIT_TIME =  os.getenv('WAIT_TIME')
    SMALL_WAIT_TIME = os.getenv('SMALL_WAIT_TIME')
    MID_WAIT_TIME = os.getenv('MID_WAIT_TIME')
    LONG_WAIT_TIME = os.getenv('LONG_WAIT_TIME')
    VERY_LONG_WAIT_TIME = os.getenv('VERY_LONG_WAIT_TIME')   
    
    def __init__(self, icognito=False):
        self.driver = None
        self.user = None
        self.default__time = self.WAIT_TIME
        self.icognito = icognito
    
    def open(self, user):
        
        try:
            self.user = user
            print(f'{self.user}: opening browser instance')
            options = uc.ChromeOptions()
            options.add_argument(f'--user-data-dir={os.getenv("USER_DATA_DIR")}')
            options.add_argument(f'--lang={os.getenv("BROWSER_LANGUAGE")}')
            
            if (self.icognito):
                options.add_argument('--icognito')
            
            options.headless = False
            self.driver = uc.Chrome(options=options, use_subprocess=True)
            
        except Exception as e:
            print(f'{self.user}: error opening browser retrying in 10 seconds...')
            self.quit()
            time.sleep(10)
            self.open(self.user)