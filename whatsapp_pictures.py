from selenium import webdriver
from time import sleep

driver= webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group:')
filepath = input('Enter your filepath:')
input('Enter anything affter scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
attachment_box.click()

image_box = driver.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(1)

send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
send_button.click()

                                          
print("Success")
    
