import sys
from selenium import webdriver
from os import rename
from time import sleep
from subprocess import Popen, PIPE
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# CONSTS
ORIGIN = "https://silbebysilvy.com/my-account/"
USERNAME = "andrea.c.zurita11@gmail.com"
PASSWORD = "Andrea.zurita123"
COURSES_PAGE= "https://silbebysilvy.com/courses/reto-beyou-y-beyou-360/"

def login(driver):
    driver.get(ORIGIN)
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    checkbox = driver.find_element_by_id("rememberme")
    login_button = driver.find_element_by_name("login")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    checkbox.click()
    login_button.click()
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Andrea Zurita')]")))


def get_video_urls(driver):
    driver.get(COURSES_PAGE)
    videos = driver.find_elements_by_css_selector("a.ld-item-name.ld-primary-color-hover")
    return [video.get_attribute('href') for video in videos]

def record(driver, videos):
    for i,video in enumerate(videos):
        driver.get(video)
        entry_title = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.entry-title')))

        s = 0
        process = Popen('screencapture -gv videos/temp.mov', shell=True, stdin=PIPE) # Start recording
        
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        play_button = driver.find_element_by_css_selector("#player > div.vp-controls-wrapper > div.vp-controls > button > div.play-icon")
        full_screen = driver.find_element_by_css_selector("button.fullscreen") 
        progress = driver.find_element_by_css_selector("div.vp-progress > div.played")

        play_button.click()
        full_screen.click()

        finished = False
        while not finished:
            finished = progress.get_attribute("style") == "width: 100%;"

        driver.switch_to.default_content()
        process.stdin.close()

        sleep(2)
        new_name = 'videos/' + str(i) + '_' + entry_title.text + '.mov' 
        rename('videos/temp.mov', new_name)

    driver.close()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    login(driver)
    videos = get_video_urls(driver)
    record(driver, videos)
   
