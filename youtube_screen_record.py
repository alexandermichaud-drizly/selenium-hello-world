from selenium import webdriver
from time import sleep
test_url = "https://youtu.be/5Yu9UBKCwOY"
import sys

driver = webdriver.Chrome()
driver.get(test_url)
video = driver.find_element_by_id("player-container-outer")
s = 0
video.click()
while not driver.execute_script('return document.getElementsByTagName("video")[0].ended'):
    sys.stdout.write(f'Recording time: {s} secs')
    sys.stdout.flush()
    sleep(1)
    for _ in range(22):
        sys.stdout.write('\b')
    s += 1

driver.close()
