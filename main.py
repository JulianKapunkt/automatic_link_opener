from selenium import webdriver
from selenium.webdriver.common.keys import Keys

linkliste = "links.txt"
chrome_driver_path = r"C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

with open(linkliste, mode="r") as f:
    data = f.readlines()
    links = [line.strip() for line in data]

    driver.get(links[0])
    
    for link in links[1:]:
        driver.execute_script('window.open("{}", "_blank");'.format(link))
        
        

