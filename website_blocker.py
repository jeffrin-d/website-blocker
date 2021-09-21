import time
from datetime import datetime as dt


hosts_path="/private/etc/hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_list=[]

while True:
    if 8 < dt.now().hour < 20:
        print("Working hours...refrain from distractions")
        with open(hosts_path, 'r+') as file:
            content=file.read()
#           print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hosts_path, 'r+') as file:
            lines=file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)