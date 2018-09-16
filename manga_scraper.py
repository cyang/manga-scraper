from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import codecs
import os

URL = "https://manganelo.com/chapter/read_slam_dunk_manga/chapter_"
MANGA_TITLE = "Slam Dunk"
MANGA_PATH = MANGA_TITLE.lower().replace(" ", "_")
SAVE_PATH = "/Users/ChrisYang/Desktop/" + MANGA_PATH
CHAPTER_BEGIN = 1
CHAPTER_END = 276

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# the page is ajaxy so the title is originally this:
print "Downloading " + MANGA_TITLE + " from chapter " + str(CHAPTER_BEGIN) + " to " + str(CHAPTER_END)

try:
    for chapter in range(CHAPTER_BEGIN, CHAPTER_END + 1):
        # go to url
        driver.get(URL + str(chapter))

        # Save page as
        complete_name = os.path.join(SAVE_PATH, MANGA_PATH + "_" + str(chapter) + ".html")
        file_object = codecs.open(complete_name, "w", "utf-8")

        html = driver.page_source
        file_object.write(html)

        print str(round(float(chapter)/CHAPTER_END, 2)) + "%: Downloaded " + MANGA_TITLE + " chapter " + str(chapter) 
finally:
    driver.quit()
