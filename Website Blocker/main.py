import time
from datetime import datetime as dt

print("Please Change Host_temp to hots_path so you can use with better Experience")
time.sleep (2)

hosts_temp=r"C:\Users\Windows 10\Desktop\Website Blocker\hosts"

#hosts_path="/etc/hosts"

redirect="127.0.0.1"

website_list=["www.pornhub.com","pornhub.com","dub119.mail.live.com","www.dub119.mail.live.com"]

working_hours = {
    'start': dt(dt.now().year, dt.now().month, dt.now().day, 9),
    'stop': dt(dt.now().year, dt.now().month, dt.now().day, 17)
}

while True:

    if working_hours['start'] < dt.now() < working_hours['stop']:


        print("Working...")

        with open(hosts_temp,'r+') as file:

            content=file.read()

            for website in website_list:

                if website in content:

                    pass
                else:

                    file.write(redirect+" "+ website+"\n")


    else:

        with open(hosts_temp,'r+') as file:

            content=file.readlines()

            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):

                    file.write(line)

            file.truncate()

        print("Your Computer is Now Protected From Spam Websites ")
    time.sleep(5)
