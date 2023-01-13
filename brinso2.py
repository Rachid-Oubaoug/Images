import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('headless')

#chrome
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/autorun/Downloads/chromedriver 5")
driver = webdriver.Chrome(options=options,executable_path = DRIVER_BIN)


#edge
#driver = webdriver.Edge(r"/Users/autorun/Downloads/edgedriver_mac64_m1/msedgedriver")
agent = driver.execute_script("return navigator.userAgent")
print (1,agent)

file=open("domains.txt")

domains=file.readlines()

for d in domains:
	driver.get('https://brinso.com/tool/premium/')
	d=d.strip()
	d=d.replace(".com","")
	file_object = open('brinsoresults.txt', 'a')
	driver.find_element("name",'brand_name').send_keys(d)
	driver.find_element("name",'my_category').send_keys("Other")
	l= driver.find_element("xpath", '//*[@id="form-total"]/div[2]/center/input')
	element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-total"]/div[2]/center/input')))
	l.click()
	valeur=driver.find_element("xpath", '//*[@id="demo"]/center/div')
	try:
		value=str(valeur.text).replace("%","")
		if int(value) > 93:
			print (d+","+value)
		file_object.write(d+".com,"+value+'\n')
		file_object.close()
	except Exception as e:
		print (d+","+str(e))
		file_object.write (d+".com,"+str(e)+'\n')
		file_object.close()
		pass
	time.sleep(2)

driver.quit()
