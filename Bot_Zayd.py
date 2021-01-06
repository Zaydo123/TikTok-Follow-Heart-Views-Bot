import pyfiglet, os, sys, random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent
from time import sleep
from os import system

# This is a branch made by Zaydo123
# I made this branch to prevent getting blocked from https://vipto.de/
# After extensive use I started getting blocked by cloudflare, so this is my solution :)
# if anyone would like, i'd also made it easier to thread this program if you'd like. 
# I'm also too lazy to implement the use of proxies, but i reccomend you use a vpn while using this script for max effectiveness. 
# For some reason mac spoofer is acting up, so i commented it out. 


class Tiktokbot:

    def __init__(self):
        if os.path.exists('proxies.txt') != True:
            with open('proxies.txt','w+'):
                print("[Made Proxy File] Quitting!")

        with open('proxies.txt','r') as f:
            self.chrome_options = webdriver.ChromeOptions()
            proxyYorN = input("Would you like to use proxies?: ")
            for _ in str(proxyYorN):
                if _ == 'Y' or _ == 'y':
                    proxy_list = f.read().split('\n')
                    if proxy_list[0] == '':
                        print("Please Fill The 'proxies.txt' file with proxies")
                        print("It is recommended you use residential proxies.")
                        sleep(3)
                        exit()
                    rand_proxy = random.choice(proxy_list)
                    #proxy_type = input('Proxy Type [socks5,http,etc...]: ')
                    #PROXY = {proxy_type:rand_proxy}
                    PROXY = rand_proxy
                    print(PROXY)
                    self.chrome_options.add_argument(f'--proxy-server={PROXY}')
                    sleep(1)
                else:
                    self.total = 0
                    operating_system = sys.platform
                    if operating_system == 'win32':
                        system("cls")
                        #os.system('spoof-mac.py randomize wi-fi')
                    else:
                        system("clear")
                    tiktokbot = pyfiglet.figlet_format("NoNameoN", font="slant")
                    print(tiktokbot)
                    print("Author: https://github.com/NoNameoN-A")
                    print("https://www.tiktok.com/@social_degradation_crazy/video/6898692248968400130")
                    self.ua = UserAgent()
                    self.ua = self.ua.random
                    self.chrome_options.add_argument('--no-sandbox')
                    self.chrome_options.add_argument('--disable-dev-shm-usage')
                    self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.chrome_options.add_argument(f'user-agent={self.ua}')
                    self.driver = webdriver.Chrome(options=self.chrome_options)
                    self.driver.minimize_window()
                    self.vidUrl = input('Video URL: ')
                    self.action = input("""
===========================        
[1] Views                 |
[2] Hearts                |
[3] followers             |
[4] (FIRST) comments heart|
===========================
[>] """)
                    self.driver.get("https://vipto.de/")
                    self.driver.maximize_window()


    def up_count(self):
        self.total+=500

    def loop1(self):
        sleep(10)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
            self.driver.minimize_window()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            self.driver.refresh()
            loop1()
        try:
            sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            self.driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
            sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
            sleep(10)
            self.driver.refresh()
            self.up_count()
            print("Views success delivered! Total", self.total,"views")
            sleep(80)
            loop1()
        except:
            print("An error occured. Now will retry again")
            self.driver.refresh()
            sleep(20)
            loop1()

    def loop2(self):
        sleep(10)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
            self.driver.minimize_window()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            self.driver.refresh()
            loop2()
        try:
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
            sleep(10)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
            sleep(10)
            hearts = self.driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
            sleep(55)
            print(hearts," Success delivered!")
            sleep(100)
            self.driver.refresh()
            sleep(200)
            loop2()
        except:
            print("An error occured. Now will retry again")
            self.driver.refresh()
            sleep(355)
            loop2()

    def loop3(self):
        sleep(10)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
            self.driver.minimize_window()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            self.driver.refresh()
            loop2()
        try:
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/input").send_keys(vidUrl)
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/div/button").click()
            sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
            sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
            sleep(47)
            self.driver.refresh()
            loop3()
        except:
            print("An error occured. Now will retry again")
            self.driver.refresh()
            sleep(50)
            loop3()

    def loop4(self):
        sleep(20)
        wait_time = 660 #11 minutes
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
            self.driver.minimize_window()
        except:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
            self.driver.refresh()
            loop4()
        try:
            sleep(20)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
            sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
            sleep(20)
            self.driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
            sleep(wait_time/3)
            print("Success delivered")
            sleep(wait_time/3)
            self.driver.refresh()
            sleep(wait_time/3)
            loop4()
        except Exception as e:
            print("Oops!", e, "occurred.")
            print("An error occurred. Now will retry again")
            self.driver.refresh()
            sleep(wait_time)
            loop4()

if __name__ == "__main__":

    Viewbot = Tiktokbot()
    bot = Viewbot.action

    if bot == 1:
        Viewbot.loop1()
    elif bot == 2:
        Viewbot.loop2()
    elif bot == 3:
        Viewbot.loop4()
    else:
        Viewbot.loop3()
