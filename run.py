import requests
from datetime import datetime
import random
import time
import sys

def set_step(username: str, password: str, step: str):
    url = "https://service-hg5j94iz-1254563013.sh.apigw.tencentcs.com/release/change_step_test"
    params = {
        "user": username,
        "password": password,
        "step": step
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "service-hg5j94iz-1254563013.sh.apigw.tencentcs.com",
        "Pragma": "no-cache",
        "Referer": "https://shua.iifxs.xyz/",
    }
    for _ in range(5):
        response = requests.get(url, headers=headers, params=params)
        text_data = response.text
        if "success" in text_data:
            return 1
        else:
            time.sleep(10)
            continue
    return None

def main(username, password, start_step):
    step = start_step
    while True:
        if datetime.now().hour==8:
            if datetime.now().weekday() in [1,2,3,4,5]: # 工作日
                step = step + random.randint(88, 666)
                res = set_step(username, password, str(step))
                if res == 1:
                    print("{},{}点了，步数{}".format(datetime.now().date(),datetime.now().hour,step))
                else:
                    print("失败了，请稍后再试")

        elif datetime.now().hour==12:
            step = step + random.randint(500, 1000)
            res = set_step(username, password, str(step))
            if res == 1:
                print("{},{}点了，步数{}".format(datetime.now().date(),datetime.now().hour,step))
            else:
                print("失败了，请稍后再试")

        elif datetime.now().hour==18:
            step = step + random.randint(500, 1000)
            res = set_step(username, password, str(step))
            if res == 1:
                print("{},{}点了，步数{}".format(datetime.now().date(),datetime.now().hour,step))
            else:
                print("失败了，请稍后再试")
                
        time.sleep(4000)


if __name__ == '__main__':

    username = "你自己的用户名"
    password = "你自己的密码"
    step = 1978 # 起始步数

    main(username, password, step)
        
