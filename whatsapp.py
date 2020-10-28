from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group:')
msg = input('Enter your message:')
count = int(input('Enter the count:'))