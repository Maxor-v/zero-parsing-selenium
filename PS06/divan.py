import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)

    # yield {
    #     'name': lamp.css('div.lsooF span::text').get(),
    #     'price': lamp.css('div.pY3d2 span::text').get(),
    #     'url': lamp.css('a').attrib['href']
    # }

divans = driver.find_elements(By.CSS_SELECTOR, 'div.LlPhw')
parsed_data = []

i=0
for divan in divans:
    i = +1
    try:
        product_name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        product_price = divan.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        product_link = divan.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except Exception as e:
        print(f"{i} Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([product_name, product_price, product_link])

driver.quit()

print(parsed_data)

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название дивана', 'Цена', 'Ссылка на диван'])
    writer.writerows(parsed_data)