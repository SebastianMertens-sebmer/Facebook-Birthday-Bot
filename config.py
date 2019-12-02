#!/usr/bin/env python
# -*- coding: utf-8 -*-

#First projekt catchPi
import re
import time
import pickle
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .urls import get_facebook_url
from .urls import get_facebook_url_wish
from .urls import get_events

persons = []


class Facebook:

    def __init__(self, headless):
        # firefox initialization
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        if headless is True:
            options.add_argument('headless')
            options.add_argument('--no sandbox')
            options.add_argument('window_size=1024x768')
        self.driver = webdriver.Chrome('./assets/chromedriver',
                                       chrome_options=options)

        """firefox_options = Options()
        if headless:
            firefox_options.add_argument("-headless")
        
        self.driver = webdriver.Firefox(
            headless, executable_path='/home/user/folder/assets/geckodriver')"""

#    def init_firefox(self, headless=False):
        """ Setup and Initialize Firefox Browser """

        """firefox_profile = webdriver.FirefoxProfile()
        # set English language
        firefox_profile.set_preference("intl.accept_languages", "en-US")

        # set user agent
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0"
        firefox_profile.set_preference(
            "general.useragent.override", USER_AGENT)

        if proxy_address and proxy_port:
            firefox_profile.set_preference("network.proxy.type", 1)
            firefox_profile.set_preference("network.proxy.http", proxy_address)
            firefox_profile.set_preference(
                "network.proxy.http_port", int(proxy_port))
            firefox_profile.set_preference("network.proxy.ssl", proxy_address)
            firefox_profile.set_preference(
                "network.proxy.ssl_port", int(proxy_port))
        """

    def login(self, user, passwd):
        self.driver.get(get_facebook_url())
        #add cookie for
        try:

            cookie_name = "cookies_" + str(user.split("@")[0]) + ".pkl"
            cookies = pickle.load(open(cookie_name, "rb"))
            for cookie in cookies:
                if 'expiry' in cookie:
                    del cookie['expiry']
            self.driver.add_cookie(cookie)
            print("Added cookie")
            cookie = True
        except:
            print("No Cookie - trying without")
            cookie = False
            print('reload page without cookie')
        time.sleep(5)
        self.driver.get(get_facebook_url())
        time.sleep(10)
        user_field = self.driver.find_element_by_xpath("//input[@id='email']")
        ActionChains(self.driver).move_to_element(user_field).click().perform()
        time.sleep(2)
        if cookie is True:
            n = len(user)
            x = 1000
            print(n)
            while n > 0:
                ActionChains(self.driver).send_keys(Keys.BACK_SPACE).perform()
                ActionChains(self.driver).send_keys(Keys.DELETE).perform()
                n = n - 1
                x = x - 1
                if n == 0:
                    break
                if x == 1:
                    break
            print('Loop ended.')
        time.sleep(2)
        ActionChains(self.driver).send_keys(user).perform()
        time.sleep(1)
        passwd_field = self.driver.find_element_by_xpath("//input[@id='pass']")
        ActionChains(self.driver).move_to_element(
            passwd_field).click().send_keys(passwd).perform()
        self.driver.find_element_by_id('loginbutton').click()
        print("You are now logged in")
        time.sleep(3)

    def security(self):
        print("Some humanlike interaction for your own safty")
        self.driver.get(get_events())
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1080)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 2160)")
        time.sleep(3)
        #sometimes when the birthdaypage is directly locked up it throws a fraudprevention warning (going to fix this soon)
        """try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, "myDynamicElement"))
        finally:
            return True"""

    def persons(self, personexists):
        self.driver.get(get_facebook_url_wish())

     #       persons = []
     #       birthday_today_card = self.driver.find_element_by_xpath(
     #           '//*[@id="birthdays_content"]/div[1]/div[2]/ul')
     #       for person in birthday_today_card:
     #
     #       for person in birthday_today_block:
     #       person = self.driver.find_elements_by_class_name('clearfix _691z').get_attribute()
     #           if:
     #               person is
     #       persons.append(person)
     #       print (persons)
        time.sleep(10)
        elements = self.driver.find_elements_by_tag_name("textarea")
        if not elements:
            print("No element found")
        else:
            return personexists == True

        if personexists == True:
            content_blocks = self.driver.find_elements_by_xpath(
                '//*[@id="birthdays_content"]/div[1]/div[2]/ul')
            global persons
            time.sleep(3)
            for block in content_blocks:
                elements = block.find_elements_by_css_selector('a')
                for el in elements:
                    persons.append(el.get_attribute("title"))
            persons = [x for x in persons if x != '']
            return persons

    def wishes(self, greetings, tag, user):
        self.driver.get(get_facebook_url_wish())
        time.sleep(10)
        wishbox = self.driver.find_elements_by_tag_name("textarea")
        boxIndex = 0
        person_index = 0
        global persons

        if len(wishbox) == len(persons):
            tag == True
        else:
            tag == False

        for commentBox in wishbox:
            boxIndex += 1
            try:
                commentBox.click()
                print('clicked a birthday-box')
                time.sleep(2)
                if (self):
                    #maybe better click person and loop threw persons pages and post directly and timeline
                    time.sleep(2)
                    commentInput = self.driver.find_element_by_tag_name(
                        "textarea")
                    ActionChains(self.driver).move_to_element(
                        commentInput).click()
                    if tag is True and len(persons) != person_index:
                        """need to fix mark down"""
                        ActionChains(self.driver).send_keys(
                            '@' + persons[person_index]).send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()
                        time.sleep(2)
                        commentInput.send_keys(' ')
                        commentInput.send_keys(greetings)
                        person_index += 1
                    else:
                        commentInput.send_keys(greetings)
                    print('worked')
                    commentInput.submit()
                    time.sleep(2)
                    print('wished happy bday')
            except:
                time.sleep(2)
                print("no wishes today!")
                continue
        pickle.dump(self.driver.get_cookies(), open(
            "cookies_" + str(user.split("@")[0]) + ".pkl", "wb"))
        return None

    def telegram_bot_sendtext(self, bot_token, bot_chatID, telegram, personexists):
        if telegram and personexists is True:
            ts = time.time()
            timestamp = str(datetime.datetime.fromtimestamp(
                ts).strftime('%d.%m.%y at %H:%M:%S'))
            if len(persons) > 0:
                bot_message = "Persons wished happy birthday: " + \
                    str(', '.join(persons)) + '\n' + \
                    "Congrats timestamp: " + timestamp
            else:
                bot_message = "No birthdays today" + '\n' + \
                    "Timestamp of execution: " + timestamp
            # Customize your message
            print("Sending message telegram")
            send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

            response = requests.get(send_text)
            return response.json()
        else:
            None

    def whatsapp_message(self, telnumber):
        pass

    def close(self):
        print('closing session in:')
        range = [1, 2, 3, ]
        for x in range:
            print(x)
            time.sleep(1)
        print('closing session now')
        self.driver.close()
#next idea is to make the bot send messages to me whom i wished happyB
#next step is then to send me yes or no options in telegram if i want to wish happyb or not
#Ideas to work on
#       now wishes needs to repeat till it doesnt find anymore "textArea"
#       //*[@id="birthdays_content"]/div[1]  it should find the amount of People / "textArea"s in this and exactly this often repeat to post the greetings
#       if amount people is not equal amout of text boxes it should find the person "who blocked their time line" and write them a PM
