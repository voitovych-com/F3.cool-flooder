from user_agent import generate_user_agent
import time
import requests
import re

f3 = 'http://f3.cool/api/v1/users/{Your user id}/questions' #User id you have must get with POST requests to send questions

head = {
    'Host': 'f3.cool',
    'Accept': 'application/json, text/plain, */*',
    'X-App-Version': 'F3-Web/v1.9.9',
    'Origin': 'https://f3.cool',
    'User-Agent': generate_user_agent(),
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'locale=en_US; _ga=GA2.1.2225661410.1573775603; _gid=GA1.4.918322528.1571775613'
}

proxy = [
    'http://165.22.184.132:80',
    'http://151.80.199.89:3128',
    'http://167.172.128.249:80',
    'http://146.185.192.26:3128',
    'http://67.205.184.39:3128',
    'http://68.183.53.79:8080',
    'http://159.203.34.129:8080',
] # Your proxy list

payload = { 'text': 'мяу мяу...' }

send=0
error=0
proxy_error=0
rp=None
f3rp=None
for i in range(0,50):
    for p in proxy:
        time.sleep(5)
        proxies = {'http': p}
        try:
            response_check = requests.get('http://ip-api.com/json/?fields=query', headers={'User-Agent': generate_user_agent()}, proxies=proxies).text
            rp=response_check
            result = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", p)
            if str(result.group(0)) in str(rp):
                response = requests.post(f3, data=payload, proxies=proxies, headers=head)
                f3rp=response.text
                if response.status_code==204:
                    send+=1
                else:
                    error+=1
            else:
                proxy_error+=1
        except IOError:
            proxy_error+=1

        print('Send: {0}. Error: {1}. Proxy Error: {2}. Proxy response: {3}. F3 response: {4}'.format(send, error, proxy_error, rp, f3rp))
    
