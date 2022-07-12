#BatchInstall.py
import os
homebrews = {"anki",}
try:
    for homebrew in homebrews:
        os.system("brew install "+homebrew)
    print("Successful")        
except:
    print("Failed Somehow")
