from selenium import webdriver

#Chooses browser-type
driver = webdriver.Chrome()

#Defines Playlist
driver.get('https://www.youtube.com/playlist?list=PLBgeu_-TzvHfABlVOp3BD-ZozTyz3loNu')

#Accepts cookies for this browser instance
cookieAllow = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
cookieAllow.click()

#Starts Playlist
playlistStart = driver.find_element_by_xpath('//*[@id="thumbnail"]')
playlistStart.click()

#Gets link of first video in list
lastLink = driver.current_url

#Goes to download-site
driver.get('https://ytmp3.cc/en16/')

#Fixes required inputs
downloadField = driver.find_element_by_xpath('//*[@id="input"]')
downloadField.send_keys(lastLink)

convertButton = driver.find_element_by_xpath('//*[@id="submit"]')
convertButton.click()

downloadButton = driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
downloadButton.click()