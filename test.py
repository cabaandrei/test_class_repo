from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

my_driver = webdriver.Chrome(service=Service('chromedriver.exe'))
# my_driver.get("https://cnn.com")
my_driver.get("D:/ACaba/classes/Leson 4/tip_calc/tip_calc/index.html")
# my_driver = Chrome(chrome_options=options)
# my_driver.find_element(By.ID, 'billamt').send_keys(160)
# my_driver.find_element(By.ID, 'billamt').send_keys(160)
my_driver.find_element(By.XPATH,'//*[@id="billamt"]').send_keys("160")

# my_driver.find_element(By.ID,value='serviceQual').send_keys("1")
my_driver.find_element(By.XPATH,'//*[@id="serviceQual"]/option[4]').click()

my_driver.find_element(By.ID,value='peopleamt').send_keys("4")


# my_driver.find_element(By.ID,value='peopleamt').send_keys(Keys.RETURN)
# my_driver.find_element(By.ID,value='calculate').send_keys(" ")
my_driver.find_element(By.ID,value='calculate').click()
result = my_driver.find_element(By.ID,value='tip').text
print(f'result is {result}.')
# if float(result) < 5:
#     print('Why are you tipping so little?')
# else:
#     print("You're generous!")
assert result == '6.00'
input()
my_driver.close()
