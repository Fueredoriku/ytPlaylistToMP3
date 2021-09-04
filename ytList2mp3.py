from selenium import webdriver

#Chooses browser-type
driver = webdriver.Chrome()

#Defines Playlist
driver.get('https://www.youtube.com/playlist?list=PLBgeu_-TzvHfABlVOp3BD-ZozTyz3loNu')

#Accepts cookies for this browser instance
cookieAllow = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
cookieAllow.click()
