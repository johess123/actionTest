import datetime

def main():
	print("push 觸發")
	with open('test2.txt', 'a') as f:
		f.write("push 時間:"+str(datetime.datetime.now())+"\n")
		f.write("-------------------------------------\n")

main()