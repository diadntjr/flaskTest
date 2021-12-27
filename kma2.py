from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for item in soup.select("item"):
    print(item.select_one("title").string)
    
for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()
    
print(soup.select_one("title").string)
print("날짜:", location.select_one("tmEf").string)
print("지역:", soup.select_one("province").string)