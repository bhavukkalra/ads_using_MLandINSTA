from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
    
        self.username = username
        self.password = password 
        # a variable to catch the instance returned by webdriver
        self.driver = webdriver.Chrome('./chromedriver') 
        self.login()
          





    #future passing login and password  
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/') 
        # self.driver.find_element_by_name('username').send_keys(self.username)
        # self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)






# runs only when module itself is runned main not when it is imported
# __main__ == 'module_name'
if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')
    print(ig_bot.username)
