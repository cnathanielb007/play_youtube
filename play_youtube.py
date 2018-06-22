#for playing a particular video from youtube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys






search_query="www.youtube.com/results?search_query="

song_name= input("what is your song name")

length=len(song_name.split())
if (length != 1):
    wordsplit = song_name.split()
    q=''
    ln=length-1
    for n in ln:
        q + "+" + wordsplit[n]
    search_query + q
else:
    search_query + "+" + song_name

    
driver = webdriver.Firefox()
driver.get(search_query)
link = driver.find_element_by_id("video-title")
link.click()
