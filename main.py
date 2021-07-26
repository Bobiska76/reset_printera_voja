from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import random

# ------------- kuca slovo po slovo kao covek  ----

#def hand_typed_comment(comment, field):
#    for i, v in enumerate(comment):
#        field.send_keys(v)
#        sleep(random.random() / 3)

# -------------------------------------------------------

binary = FirefoxBinary('/usr/bin/firefox')                # poziva firefox za windows drugacija putanja
browser = webdriver.Firefox(firefox_binary=binary, executable_path="/home/kali/Desktop/geckodriver")  # ucitava drajver za citanje u mozili
browser.implicitly_wait(5)                      # ceka pet sec za svaki slucaj dok ucita stranu

browser.get('https://192./')    # hardcode uneti adresu na kojoj je stampac, za sada jednu, ako radi ici ce lista adresa ili ce vaditi iz csv

sleep(2)

not_now_btn = browser.find_element_by_xpath("//button[text()='Not Now']")
not_now_btn.click()

sleep(2)

not_now_btn = browser.find_element_by_xpath("//button[text()='Not Now']")
not_now_btn.click()

sleep(2)


username_input = browser.find_element_by_css_selector("input[name='username']")     # trazi na stranici element username
password_input = browser.find_element_by_css_selector("input[name='password']")     # trazi pass polje


username_input.send_keys("***************")    # hardcode uneti username
password_input.send_keys("***************")    # hardoce password 


login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)


browser.get('https://ipadresa strane za reset dugme/')

sleep(3)

reset_printer = browser.find_element_by_xpath("//button[@type='reset printer']")
login_button.click()







#browser.close()