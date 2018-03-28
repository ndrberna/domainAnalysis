"""
Parallel image downloader"""

import os
import urllib2
import time
from contextlib import closing
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

OPTIONS = Options()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--window-size=1920x1080")
CHROME_DRIVER = os.getcwd() +"/chromedriver"

LINES = ""
DIRECTORY = "data"
IMAGE_DIRECTORY = "images"
FILENAME = "CleanDomainsRegistered2018-03-01.txt"
NUM_PROCESSES = 1
with open(DIRECTORY+"/"+FILENAME) as f:
    LINES = f.read().splitlines()
    f.close()
DIRECTORY = os.getcwd()

def parse(i):
    """ parsing module """

    if not os.path.isfile((os.getcwd()+"/"+ IMAGE_DIRECTORY +"/"+i.replace("http://www.", "")+".png")):
        driver = webdriver.Chrome(chrome_options=OPTIONS, executable_path=CHROME_DRIVER)
        try:
            urllib2.urlopen(i)
            driver.get(i)
            time.sleep(4)
            driver.get_screenshot_as_file(os.getcwd()+"/"+ IMAGE_DIRECTORY +"/"+i.replace("http://www.", "")+".png")
        except Exception, error:
            print error, str(i)
            driver.quit()
        driver.quit()



with closing(Pool(processes=NUM_PROCESSES)) as p:
    print "start downloading in directory:", IMAGE_DIRECTORY
    RECORDS = p.map(parse, LINES)
    p.terminate()
    print "downloading end"
