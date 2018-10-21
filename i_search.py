#! python3
from selenium import webdriver as wd

chrome = wd.Chrome()
chrome.get('http://google.com')
