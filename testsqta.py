from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium
import time

def login(br, user_name, pass_word):
    br.get("http://eventsforall.000webhostapp.com/")
    br.get("http://eventsforall.000webhostapp.com/")
    username = br.find_element_by_name("username")
    username.send_keys(user_name)
    password = br.find_element_by_name("password")
    password.send_keys(pass_word)
    password.send_keys(Keys.RETURN)
    time.sleep(5)
def start(user_name, pass_word):
        br = webdriver.Chrome()

    #try:
        login(br, user_name, pass_word)
    #except :
        #print("wrong details.try again")
        #login(br, user_name, pass_word)
    #try:
        br.get("http://eventsforall.000webhostapp.com/list.php")
        event_link = br.find_element_by_name("addeventlink")
        event_link.click()
        br.get("http://eventsforall.000webhostapp.com/addevent.html")
        name = br.find_element_by_name("organisername")
        name.send_keys("PCCOE")

        event_name = br.find_element_by_name("eventname")
        event_name.send_keys("Webinar")

        date = br.find_element_by_name("date")
        date.clear()
        date.send_keys('09/05/2019')

        address = br.find_element_by_name(" address")
        address.send_keys('Nigdi')

        city= br.find_element_by_name("city")
        city.send_keys("Pune")

        state = br.find_element_by_name("state")
        state.send_keys("Maharashtra")

        country = br.find_element_by_name("country")
        country.send_keys("India")

        pcode = br.find_element_by_name("postalcode")
        pcode.send_keys("411044")

        contact = br.find_element_by_name("contact")
        contact.send_keys("9598495320")

        email = br.find_element_by_name("email")
        email.send_keys("pccoe@gmail.com")

        submit = br.find_element_by_name("addevent")
        submit.click()

        time.sleep(50)


    #except:
        #print("wrong details.try again")

        #(br, user_name, pass_word)


        time.sleep(50)
        br.close()


start("dummy@gmail.com", "dummy")
