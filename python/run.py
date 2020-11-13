import os
import cv2
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException


from func import solve

#if _name_ == "_main_":
def main():
	#image name with extension
	cwd = os.getcwd()
	#imagename = "1.jpeg"
	[filename] = sys.argv[1:]
	img = cv2.imread(filename)
	y,x,r = img.shape

	crop_img = img[200:, :]
	croppath = os.path.join(cwd,"python\\1.png")
	cv2.imwrite(croppath, crop_img)
	
	#print(filename)
	#cureent path
	
	
	#filepath = os.path.join(cwd,imagename)

	#add your chrome driver path
	chromepath = os.path.join(cwd,"python\\chromedriver.exe")
	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	#chromepath = "D:\\ProgramData\\ChromeDriver\\chromedriver.exe"
	driver = webdriver.Chrome(chromepath,chrome_options=chrome_options)
	driver.get("https://www.onlineocr.net/")


	#driver.maximize_window()

	####upload image####
	#manual
	#driver.find_element_by_class_name("fileinput-button").click()
	#auto
	try:
		driver.find_element_by_id("fileupload").send_keys(croppath)
	except InvalidArgumentException:
		print("errror")
		return
	#wait 60 seconds to upload image
	submitBtn = WebDriverWait(driver, 180).until(
	EC.element_to_be_clickable((By.ID,"MainContent_btnOCRConvert")))
	submitBtn.click();

	#wait 40 seconds untils image process
	textOutput = WebDriverWait(driver, 40).until(
	 EC.presence_of_element_located((By.ID, "MainContent_txtOCRResultText")))
	txtInput = textOutput.get_attribute('value')


	matrix,words=solve(txtInput)

	#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
	# Open a new window
	#driver.execute_script("window.open('');")
	#driver.switch_to.window(driver.window_handles[1])
	driver.get("https://solver.0xcaff.me/input/text")

	WebDriverWait(driver, 40).until(
	EC.presence_of_element_located((By.CLASS_NAME, "App")))

	action = ActionChains(driver)
	action.send_keys(Keys.TAB).send_keys(matrix).send_keys(Keys.TAB).send_keys(words).perform()


	solveBtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/footer/span')
	solveBtn.click()

	print("made with love")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()