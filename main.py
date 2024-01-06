import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pymongo import MongoClient

def scrap_houses():
    url='https://zh.youlive.ca/vancouver-real-estate/'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(10)
    houses = driver.find_elements(By.CLASS_NAME, 'link-loading')  
    # Got Top 10 houses information 
    houses = houses[:10]
    house_cases=[]
    for house in houses:
        roomType=house.find_element(By.XPATH,"div[1]/div[2]/div[1]/h3/span[1]").text
        city=house.find_element(By.XPATH,"div[1]/div[2]/div[1]/h3/span[2]").text
        roomSize=house.find_element(By.XPATH,"div[1]/div[2]/div[2]/span[1]").text
        price=house.find_element(By.XPATH,"div[1]/div[2]/div[2]/span[2]").text
        # image=house.find_element(By.XPATH,"div[1]/div[1]/div[1]/div[1]/img").get_attribute('src')
        house_case={
            'roomType': roomType,
            'city': city,
            'roomSize': roomSize,
            'price': price
        }
        house_cases.append(house_case)
    driver.close()
    driver.quit()
    return house_cases

def main():
    client = MongoClient('localhost',27017)
    db = client.test_database
    collection = db.test_collection
    house_cases = scrap_houses()
    # delete all history data in mongodb
    collection.delete_many({})
    # insert data
    collection.insert_many(house_cases)
    # print(result.inserted_ids)
    # query data
    query = {'city':'西温'}
    result = collection.find(query)
    for house in result:
        print(house)
if __name__=='__main__':
    main()