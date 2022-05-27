# # ამოცანა 1
#
# from bs4 import BeautifulSoup
#
# file = open("index.html", "r")
# content = file.read()
# print(content)
# soup = BeautifulSoup(content, "html.parser")
# print(type(soup))
# print(soup.head.title)
# print(soup.h2)
# print(soup.h2.text)
# print(soup.a.attrs["href"])
# res = soup.find("ul", {"id": "list2"})
# res = soup.find("ul", id="list2")
# print(res)
# res = soup.find_all("h2")
# print(res)


# ამოცანა 2

import requests
from bs4 import BeautifulSoup
import csv

file = open("books.csv", "w", encoding="utf-8_sig", newline="\n")
# file.write("სათაური"+","+"ავტორი"+","+"ფასი"+","+"აღწერილობა"+","+"\n")
file_obj = csv.writer(file)
file_obj.writerow(["სათაური", "ავტორი", "ფასი", "აღწერილობა"])
for ind in range(1, 6):
    url = "https://www.lit.ge/index.php?page=books&send[shop.catalog][page]=" + str(ind)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    section = soup.find("section", class_="list-holder")
    # print(section)
    books = section.find_all("article")
    for book in books:
        title_bar = book.find("div", class_="title-bar")
        book_name = title_bar.a.text
        author = title_bar.b.a.text
        descr = book.p.text
        price = book.button.text.strip()
        print(price)
        # file.write(book_name + "," + author + "," + price + "," + descr + "\n")
        file_obj.writerow([book_name, author, price, descr])
file.close()