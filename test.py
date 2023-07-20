import datetime

def main():
	with open('test.txt', 'a') as f:
		f.write("現在時間:"+str(datetime.datetime.now())+"\n")
		f.write("-------------------------------------\n")

main()