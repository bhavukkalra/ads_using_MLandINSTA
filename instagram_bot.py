from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
    
        self.username = username
        self.password = password
        self.base_url = 'https://www.instsagram.com/' 
        # a variable to catch the instance returned by webdriver
        self.driver = webdriver.Chrome('./chromedriver') 
        self.login()



    #future passing login and password  
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/') 
        self.driver.find_element_by_name('username').send_keys(self.username)
        
        self.driver.find_element_by_name('password').send_keys(self.password)
        #could also be possible to find it by text if this 
        #does not work with some browsers
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

        time.sleep(2)


    def nav_user(self, user):
        self.driver.get(self.base_url + user)

    def follow_user(self, user):
        self.nav_user(user)
        #follow_user = self.driver.find_elements_by_id('$0')[0].click()
        #only button with text follow in it
        self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
        

        






# runs only when module it  self is runned main not when it is imported
# __main__ == 'module_name'
if __name__ == '__main__':
    ig_bot = InstagramBot('bhavukkalra1786', 'bhavuk1786')
#    ig_bot.nav_user('bhavukkalra1786')
    ig_bot.follow_user('garyvee')
