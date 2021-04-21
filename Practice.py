from selenium import webdriver

import time

driver=webdriver.Chrome('D:/TestPython/venv/Lib/site-packages/chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username=driver.find_element_by_xpath("//input[@id='username']")
username.clear()
username.send_keys('email')
password=driver.find_element_by_xpath("//input[@id='password']")
password.clear()
password.send_keys("password")

submit=driver.find_element_by_xpath("//button[@type='submit']").click()


#opening the connections page
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH")
time.sleep(2)

#clicking the message button in connection page
all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

for i in range(0,len(message_buttons)):
    message_buttons[i].click()
    time.sleep(2)

    #targetting message field
    main_div=driver.find_element_by_xpath("//div[starts-with(@class,'msg-form__msg-content-container')]")
    driver.execute_script('arguments[0].click();', main_div )
    paragraphs=driver.find_elements_by_tag_name("p")    #message field
    paragraphs[-5].send_keys("testing")
    time.sleep(2)

    #hitting send button after writing a message
    submit=driver.find_element_by_xpath("//button[@type='submit']")
    driver.execute_script('arguments[0].click();', submit)
    time.sleep(2)

    #closing the message screen data-control-name="overlay.close_conversation_window"
    close_button=driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
    driver.execute_script('arguments[0].click();',close_button)       #writing java code because linkedin throws a exception so we over ride it using java
    time.sleep(2)


