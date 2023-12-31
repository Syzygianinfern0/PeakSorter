import re

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

# url = "https://www.rei.com/c/mens-road-running-shoes?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-trail-running-shoes?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-hiking-boots?sort=sc_revenue"
# url = "https://www.rei.com/c/socks?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-hiking-socks?sort=sc_revenue"
# url = "https://www.rei.com/c/leg-gaiters?sort=sc_revenue"
# url = "https://www.rei.com/c/hiking-clothing-accessories?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-gloves-and-mittens?sort=sc_revenue"
# url = "https://www.rei.com/c/hiking-clothing-accessories?sort=sc_revenue"
# url = "https://www.rei.com/c/headlamps"
# url = "https://www.rei.com/c/camping-chairs?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-hats-and-headwear"
# url = "https://www.rei.com/c/mens-swimwear?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-socks?sort=sc_revenue"
url = "https://www.rei.com/c/health-and-safety?sort=sc_revenue"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
data = []
page = 1

while True:
    response = requests.get(url + f"&page={page}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".VcGDfKKy_dvNbxUqm29K")
    print(len(products))
    if len(products) == 0:
        break

    for product in products:
        # find the name using the h2 tag's text content
        brand = product.select_one(".nL0nEPe34KFncpRNS29I").text.strip()
        name = product.select_one(".Xpx0MUGhB7jSm5UvK2EY").text.strip()
        price = product.select_one(".wKj5r3LozHWJf0OtkWPp").text.strip()
        if re.search(r"Save \d+%", price):
            price = re.findall(r"\$\d+\.\d+", price)
            sale_price, price = price[0], price[1]
        else:
            sale_price = price

        reviews = product.select_one(".cdr-rating__count_13-5-2").text.strip()[1:-1]
        reviews = int(reviews)

        try:
            rating = product.select_one(".cdr-rating__caption-sr_13-5-2").text.strip().split()[7]
        except IndexError:
            rating = 0.0

        # data.append({"name": name, "reviews": reviews, "rating": rating, "price": price})
        data.append(
            {
                "brand": brand,
                "name": name,
                "reviews": reviews,
                "rating": rating,
                "sale_price": sale_price,
                "price": price,
            }
        )

    page += 1

# sort for most reviews
sorted_data = sorted(data, key=lambda x: x["reviews"], reverse=True)


console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Brand", style="dim")
table.add_column("Name", style="dim")
table.add_column("Reviews", justify="right", style="dim")
table.add_column("Rating", justify="right", style="dim")
table.add_column("Sale Price", justify="right", style="dim")
table.add_column("Price", justify="right", style="dim")

for product in sorted_data[:20]:
    table.add_row(
        product["brand"],
        product["name"],
        str(product["reviews"]),
        str(product["rating"]),
        product["sale_price"],
        product["price"],
    )

console.print(table)

# print same as csv
for product in sorted_data[:10]:
    print(
        product["brand"],
        product["name"],
        str(product["reviews"]),
        str(product["rating"]),
        product["sale_price"],
        product["price"],
        sep=",",
    )
