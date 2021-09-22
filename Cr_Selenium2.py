import requests
from bs4 import BeautifulSoup
import xlsxwriter

url="https://www.digikala.com/search/category-dishes-detergents/"
page = requests.get(url)


soup = BeautifulSoup(page.text, 'html.parser')

product = soup.find_all("div", class_="c-product-box__title")
price = soup.find_all("div", class_="c-price__value-wrapper")
rate = soup.find_all("div", class_="c-product-box__engagement-rating")

lst = []
for pro,pri,rat in zip(product,price,rate):
    lst.append([pro.text,pri.text,rat.text])

print(lst)


workbook = xlsxwriter.Workbook('Hamid.xlsx')
worksheet = workbook.add_worksheet()


row = 0
col = 0

# Iterate over the data and write it out row by row.

for pro in product:
    worksheet.write(row, col,     pro.text)
    #worksheet.write(row, col + 1, price.text)
    #worksheet.write(row, col + 2, rate.text)
    row += 1
row = 0
for pri in price:
    #worksheet.write(row, col,     pro.text)
    worksheet.write(row, col + 1, pri.text)
    #worksheet.write(row, col + 2, rate.text)
    row += 1

row = 0
for rat in rate:
    #worksheet.write(row, col,     pro.text)
    #worksheet.write(row, col + 1, pri.text)
    worksheet.write(row, col + 2, rat.text)
    row += 1
workbook.close()
