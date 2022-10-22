MR = 'NotCkracker'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==MR:
 pass
else:
    os.sys.exit()
import requests,os
from time import sleep
# Xinject 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

asci = '''

     ,     \    /      ,        
    / \    )\__/(     / \       
   /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|          |\../|              |
|           \VV/               |
|     𝑁𝑜𝑡𝐶𝑘𝑟𝑎𝑐𝑘𝑒     |
|_________________________________|
 | /\ /      \\       \ /\    | 
 |  /   V        ))       V   \  | 
 |/  `       //        '     \| 

\n\n'''
sss = '\033[92m'
dn = sss+'''
____  _____ ____  ____  ____  _____ 
/  __\/  __//  __\/  _ \/  __\/__ __\
|  \/||  \  |  \/|| / \||  \/|  / \  
|    /|  /_ |  __/| \_/||    /  | |  
\_/\_\\____\\_/   \____/\_/\_\  \_/  
                                     
   
'''
cls()
def seee():
    print(asci)
    cc = '[1] While True\n[2] Range\n';print(cc)
    ch = input('Choice : ')
    if ch=='1':
        cls()
        print(asci)
        link = input('Url FB : ')
        FullName = input('Full Name : ')
        mail = input('Email : ')
        oth = input('Other : ')
        done = 0
        while True:
            cls()
            print(dn)
            url = 'https://m.facebook.com/help/contact/209046679279097'
            data = {'crt_url' : link,'crt_name': FullName,'cf_age': '13+ years','Field255260417881843': oth,'Field166040066844792': mail,'submit':'submit'}
            req = requests.post(url,data=data,timeout=60)
            done+=1
            print(f'\032 Report Done : {done}')
            sleep(1)
            cls()
######################################################
    elif ch=='2':
        cls()
        print(asci)
        ran = int(input('[+] Range : '))
        link = input('\nUrl FB : ')
        FullName = input('Full Name : ')
        mail = input('Email : ')
        oth = input('Other : ')
        done = 0
        for i in range(ran):
            cls()
            print(dn)
            url = 'https://m.facebook.com/help/contact/209046679279097'
            data = {'crt_url' : link,'crt_name': FullName,'cf_age': '13+ years','Field255260417881843': oth,'Field166040066844792': mail,'submit':'submit'}
            req = requests.post(url,data=data,timeout=60)
            done+=1
            print(f'\032 Report Done : {done}')
            sleep(1)
    else:seee()
seee()
