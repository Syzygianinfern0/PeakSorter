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
# url = "https://www.rei.com/c/health-and-safety?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-running-and-athletic-socks?sort=sc_revenue"
# url = "https://www.rei.com/c/hiking-jackets?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-base-layers?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-neck-gaiters?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-rain-jackets?sort=sc_revenue"
# url = "https://www.rei.com/c/womens-hiking-footwear?sort=sc_revenue"
# url = "https://www.rei.com/c/sleeping-bags?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-leg-gaiters?sort=sc_revenue"
# url = "https://www.rei.com/c/leg-gaiters?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-hiking-pants?sort=sc_revenue"
# url = "https://www.rei.com/c/hiking-pants?sort=sc_revenue"
# url = "https://www.rei.com/c/eating-utensils?ir=category%3Acamp-dinnerware&r=category%3Acamp-dinnerware%7Ceating-utensils&sort=sc_revenue"
# url = "https://www.rei.com/c/mens-workout-pants"
# url = "https://www.rei.com/c/camp-towels?ir=category%3Acamp-bathroom&r=category%3Acamp-bathroom%7Ccamp-towels"
# url = "https://www.rei.com/c/tents?sort=sc_revenue"
# url = "https://www.rei.com/c/backpacking-tents?sort=sc_revenue"
# url = "https://www.rei.com/c/camping-tents?sort=sc_revenue"
# url = "https://www.rei.com/c/sleeping-pads?sort=sc_revenue"
# url = "https://www.rei.com/search?q=lantern&sort=sc_revenue"
# url = "https://www.rei.com/c/mens-hiking-jackets?ir=category%3Ahiking-jackets&r=category%3Ahiking-jackets%7Cmens-hiking-jackets&sort=sc_revenue"
# url = "https://www.rei.com/c/camp-furniture?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-running-shirts?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-running-shorts?sort=sc_revenue"
# url = "https://www.rei.com/c/mens-climbing-shoes?sort=sc_revenue"
# url = "https://www.rei.com/c/chalk-and-chalk-bags"
# url = "https://www.rei.com/c/camp-kitchen?sort=sc_revenue"
# url = "https://www.rei.com/c/stoves-and-grills?sort=sc_revenue"
# url = "https://www.rei.com/c/portable-water-treatment?sort=sc_revenue"
# url = "https://www.rei.com/c/backpacking-packs?sort=sc_revenue"
url = "https://www.rei.com/c/day-packs?sort=sc_revenue"

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "dnt": "1",
    "origin": "https://www.rei.com",
    "priority": "u=1, i",
    "referer": url,
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
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
            price = re.findall(r"\$[\d,]+\.\d+", price)
            sale_price, price = price[0], price[1]
        else:
            sale_price = price

        reviews = product.select_one(".cdr-rating__count_13-5-2").text.strip()[1:-1]
        reviews = int(reviews)

        try:
            rating = product.select_one(".cdr-rating__caption-sr_13-5-2").text.strip().split()[7]
        except IndexError:
            rating = 0.0

        link = "https://www.rei.com" + product.select_one("a").get("href")

        # data.append({"name": name, "reviews": reviews, "rating": rating, "price": price})
        data.append(
            {
                "brand": brand,
                "name": name,
                "reviews": reviews,
                "rating": rating,
                "sale_price": sale_price,
                "price": price,
                "link": link,
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
table.add_column("Link", justify="right", style="dim")

for product in sorted_data[:20]:
    table.add_row(
        product["brand"],
        product["name"],
        str(product["reviews"]),
        str(product["rating"]),
        product["sale_price"],
        product["price"],
        product["link"],
    )

console.print(table)

# print same as csv
for product in sorted_data[:20]:
    print(
        product["brand"],
        product["name"],
        str(product["reviews"]),
        str(product["rating"]),
        product["sale_price"],
        product["price"],
        product["link"],
        sep=",",
    )
