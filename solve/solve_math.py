import requests
import base64
import random
import os


##Get random captcha from test dir and solve
dir="..//test"
random_file=random.choice(os.listdir(dir))
print(random_file)

f = open(dir+"/"+random_file, "rb")
data=f.read()
#solve captcha
base64_encoded_data = base64.b64encode(data)
base64_message = base64_encoded_data.decode('utf-8')
#print(base64_message)
        
json = {"clientKey":"DEMO","task": {
"type": "ImageToTextTask",
"subType":"math",
"body": base64_message
}}
#print(json)
url_solve_captcha="http://iamnotbot.com:5000/createTask";         
r = requests.post(url_solve_captcha, json=json)
print("Captcha = "+r.text)

    
