from selenium import webdriver
import loginInfo
import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div")

login.click()

time.sleep(3)

searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
searchButton = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[1]/svg")

searchArea.send_keys("#yazilimayolver")
searchArea.send_keys(Keys.ENTER)
searchArea.send_keys(Keys.RETURN)



searchButton.click()

time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True



elements = browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")

for element in elements:
    print("***************************")
    print(element.text)

browser.close()


