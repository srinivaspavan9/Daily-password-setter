from datetime import datetime
from random import randint
import sys
today=datetime.now()

fp1=open("mypasswords.txt","a")
fp2=open("mypasswords.txt","r")
td=today.strftime("%d %B,%Y %A")

for i in range(6):
	print()

print("\t%s"%td)
print("\tWelcome Srinivas pavan")

for i in range(3):
	print()
print("Chose an option :")
while(True):
	print("\t1.Set Password")
	print("\t2.Show Password List")
	print("\t3.Exit(Press any key to exit)")
	print("\tYour option :",end=" ")
	inp=input()
	if(inp=='1'):
		pw=randint(1000,9999)
		linelist=fp2.readlines()
		lastline=linelist[-1]
		mystr=td+"  Password: "+str(pw)+"\n"
		fp1.write(mystr)
		print("Previous :",end=" ")
		print(lastline)
		print("\t\tYour new Password: %d"%pw)
		print("\t\tExit now(Yes=y/Y || No=n/N): ",end=" ")
		ex=input()
		ex=ex.upper()
		if(ex=='Y'):
			print("Pain is temporary. It may last for a minute, or an hour or a day, or even a year. But eventually, it will subside. And something else takes its place. If I quit, however, it will last forever.")
			print("Have a great day")
			sys.exit(0)
		else:
			pass
	elif(inp=='2'):
		content=fp2.read()
		print("Your Passwords :")
		print(content)
		print("\t\tExit now(Yes=y/Y || No=n/N): ",end=" ")
		ex=input()
		ex=ex.upper()
		if(ex=='Y'):
			print("Pain is temporary. It may last for a minute, or an hour or a day, or even a year. But eventually, it will subside. And something else takes its place. If I quit, however, it will last forever.")
			print("Have a great day")
			sys.exit(0)
		else:
			pass
	else:
		print("Sometimes it ain’t about being the most talented. Sometimes it ain’t about being the smartest. Sometimes it’s not even about working the hardest. Sometimes it’s about consistency! Consistency!")
		print("Have a great day")
		sys.exit(0)



