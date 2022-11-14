import requests
from bs4 import BeautifulSoup


def get_data():
    res = requests.get(
        "https://www.studyaustralia.gov.au/english/study/universities-higher-education/list-of-australian-universities",
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        },
    )

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.select_one("div.main").find_all("li")

    for item in items:
        title = str(item.text).strip().split("-")[0]
        link = item.a["href"]

        obj = {"title": title, "link": link}

        print(obj)


def main():
    print("running main")
    get_data()


main()
