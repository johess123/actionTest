import datetime
import requests
from bs4 import BeautifulSoup

def main():
	print("push 觸發時間: "+str(datetime.datetime.now()))
	print("開始爬蟲...")
	with open('url.txt', 'r') as f:
		data = f.read()
	print(data)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
	}
	r = requests.get(data, headers=headers) #將網頁資料GET下來
	soup = BeautifulSoup(r.text,"html.parser")
	articles = soup.find_all('article', class_="b-block--top-bord")
	for i in range(len(articles)):
		name = articles[i].find('a', class_="js-job-link").text
		print("----------------------------")
		print(i+1,"工作名稱",name)

main()