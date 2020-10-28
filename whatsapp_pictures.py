from selenium import webdriver
from time import sleep

driver= webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group:')
filepath = input('Enter your filepath:')
input('Enter anything affter scanning QR code')