from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bitstring import BitArray
from sys import version_info




driver_path = r"F:\\Working\\Pyton\\chromedriver_win32\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssal-errors')

driver = webdriver.Chrome(driver_path,chrome_options=options)

url="https://www.digikala.com/search/category-dishes-detergents/"

driver.get(url)

lst = []
cols = ["Product", "Price"]

#i = unicode(i, "utf-8")
name_products = driver.find_elements_by_class_name("js-product-url")
price_products = driver.find_elements_by_class_name("c-price__value-wrapper")
#what_search_box.send_keys("")



for (nam_product, price_product) in (zip(name_products, price_products)):
    lst.append((nam_product.text, price_product.text))
    print(lst)
driver.quit()

df = pd.DataFrame(lst, columns=cols)
if df.to_csv("Selenium.csv"):
    print("Sucessful")





