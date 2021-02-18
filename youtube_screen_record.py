import sys
from selenium import webdriver
from time import sleep
from subprocess import Popen
from subprocess import call

cmd = 'screencapture -v obama.mov'

test_url = "https://youtu.be/5Yu9UBKCwOY"

driver = webdriver.Chrome()
driver.get(test_url)
video = driver.find_element_by_id("player-container-outer")

s = 0
videoRecording = Popen(cmd, shell=True) # start recording
video.click()

while not driver.execute_script('return document.getElementsByTagName("video")[0].ended'):
    sys.stdout.write(f'Recording time: {s} secs')
    sys.stdout.flush()
    sleep(1)
    for _ in range(22):
        sys.stdout.write('\b')
    s += 1

sys.stdout.write('c\n')
driver.close()

