from time import sleep
import sys
from selenium import webdriver
from selenium import common

m_link = "https://play.google.com/store"
w_driver = webdriver.PhantomJS()
w_driver.set_window_size(1920, 1080)

w_driver.get(m_link)
sleep(2)

try:
    links = w_driver.find_elements_by_css_selector("a.child-submenu-link")
    #rows = w_driver.find_elements_by_css_selector(".legs-container.layout-column.flex")
except common.exceptions.NoSuchElementException:
    print "[*] Error: could not find main selector"
    sys.exit(0)


for link in links:
    title = link.get_attribute("title")
    href = link.get_attribute("href")
    print "Catagory: {0}                Link: {1}".format(title,href)

w_driver.close()
