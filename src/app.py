import os 
import time
from datetime import datetime as dt

host_path = "/etc/hosts"
host_temp = "hosts" 
# print(os.path.isfile(host_path))
# print(os.getcwd())
# os.chdir("/etc")
# print(os.getcwd())
redirect = "0.0.0.0"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com","instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # print("Its working hours, focus towards your goals")
        with open(host_temp, 'r+') as file:
            content= file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any( website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print("It's Fun hours")

    time.sleep(7)
