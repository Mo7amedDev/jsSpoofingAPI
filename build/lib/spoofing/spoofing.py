import json 
import random
import os 
from typing import Literal

def readJsonFile(file_name):
    current_dir=os.path.dirname( __file__) 
    file_path = os.path.join(current_dir,"data_spoof",file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data 


def getSpoofScript(file_name):
    current_dir=os.path.dirname( __file__) 
    file_path = os.path.join(current_dir,"jsSpoof",file_name)
    with open( file_path,'r') as f:
        spoof_js = f.read()
    return spoof_js

def spoofUserAgent(browser:Literal["chrome","firefox"]):
   
    data = readJsonFile("user-agents-chrome.json") if browser =="chrome" else readJsonFile("user-agents-firefox.json")
     
    laptops = ["macos","windows","linux"] 
    key=random.choice(laptops)
     
    userAgent = random.choice(data[key])
    script = getSpoofScript("spoof_useragent.js").replace("$userAgent$",userAgent)
    return script,userAgent

def spoofDimen():
    data = readJsonFile("dimen.json")
    dimens = random.choice(data["laptop_pc"])
   
    w,h = int(dimens["width"]),int(dimens["height"])
     
    script = getSpoofScript("spoof_dimen.js").replace("$spfw$",str(w)).replace("$spfh$",str(h))
    # view port width and height
    return script,w-40,h-100 

def spoofCanvas():
    return getSpoofScript("spoof_canvas.js")

def spoof_connection():
    return getSpoofScript("spoof_conn.js")

def spoof_font():
    return getSpoofScript("spoof_font.js")

def spoofTimeZone():
    data = readJsonFile("time_zone_logic.json")
    timeZone = random.choice(data["morroco"])

    script = getSpoofScript("spoof_timezone.js").replace("$timezone$",timeZone)
    return script,timeZone 

def spoofLanguage():
    languages = ["en-US", "en-GB", "fr-FR", "de-DE", "es-ES", "it-IT", "ja-JP", "zh-CN", "ru-RU", "ar-SA"]
    selected_language = random.choice(languages)
    script = getSpoofScript('spoof_language.js').replace("$lang$",selected_language)
    return script,selected_language

def spoofLocation():
    data = readJsonFile('location.json')
    location = random.choice(data['morroco'])
  
    lat,lon =  str(location["latitude"]),str(location["longitude"])
    script = getSpoofScript("spoof_location.js").replace("$latitude$",lat).replace('$longitude$',lon)
    return script,location["latitude"],location["longitude"]


 

 