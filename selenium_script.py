import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time, os
from selenium.common.exceptions import NoSuchElementException


def run_browser(chrome_path, args):
    import subprocess
    command = [chrome_path] + args
    subprocess.Popen(command)


def get_weibo_cookie_by_selenium(debugger_address="127.0.0.1:9222"):
    options = Options()

    options.add_experimental_option("debuggerAddress", debugger_address)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    browser = webdriver.Chrome('./chromedriver', options=options)

    browser.get("https://weibo.com/")
    time.sleep(10)
    cookie_items = browser.get_cookies()
    cookies = ""
    for item in cookie_items:
        cookie = f"{item.get('name')}={item.get('value')};"
        cookies = cookies + cookie

    browser.close()
    browser.quit()
    return cookies


def send_cookie(cookie, url):
    response = requests.post(url, data={"cookie": cookie})
    if response.status_code == 200:
        print("success")
    else:
        print("failed")


if __name__ == '__main__':
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    args = ["--remote-debugging-port=9222", '--user-data-dir=/Users/l3n641/code/weibo/data']
    url = "http://127.0.0.1:5000/cookie"

    run_browser(chrome_path, args)
    cookie = get_weibo_cookie_by_selenium()
    #cookie="XSRF-TOKEN=duNN22GbAvrUUE0vJuQYNAZY;SCF=AifpCij-SUuUemezomz-E3KHIPwjR1H_BIN3mFkmkqfSQO3OIEJ_12efdIsF-kk-Xp-hfO9Ewvi9Wm7mUPcWf1c.;SUB=_2A25MASp1DeRhGedM6VMZ8yzEyjmIHXVvdxy9rDV8PUNbmtB-LValkW9NWfioTDDstF8EuFuCsu9ONAuuPaHr7z28;SSOLoginState=1627740708;ALF=1659276708;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QpfzJ-EZMy3RD7b0Q4WGu5JpX5KMhUgL.Fo2Eeo2Re0zReK-2dJLoIE-LxK-L1hqLBoMLxKML1hnLBo8ki--RiK.NiKysi--fi-isiKn0;ULV=1627735233193:1:1:1:9570313716402.605.1627735233186:;WBPSESS=5jG0RXU0RZLYSjEfucPE52y_9hG6F2bX-pA9eUIt19_TTpqX9VlPBal1_WEbqY66LxclKKt7ikoKbju-bE9UtiQBpF2dCb1H_88QbCiPr3HxGAaokbWUvLC1VOgmlYTg;SINAGLOBAL=9570313716402.605.1627735233186;wb_view_log=1680*10502;"
    send_cookie(cookie, url)
