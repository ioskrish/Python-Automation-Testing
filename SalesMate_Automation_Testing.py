from turtle import down
import pyautogui
pyautogui.FAILSAFE = False
from win32api import GetSystemMetrics
import os
print("SalesMate Automation Testing")

print("Creating Database Backup Directory called SMP")

path="D:/KTS Infotech/PythonAutomation/SMP"
if not os.path.exists(path):
    os.makedirs(path)

#width and height
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

print("Launching Start Menu")
pyautogui.click(0,height,1,1.0)

print("Selecting SalesMate+ Application")
pyautogui.typewrite("SalesMate +",0.5)

print("For SalesMate+ to Launch properly,Extending Time delay to 10sec")
pyautogui.press("enter",1,7)

print("Canceling the setup wizard")
pyautogui.typewrite("c",5)

print("Closing Tip of the Day Dialog")
pyautogui.press("enter",1,1.0)

print("Opening Help Dialog box")
pyautogui.press(['alt','h'],1,3.0)
pyautogui.press("h",1,2.0)
pyautogui.press(['alt','Space'],1,1.0)
pyautogui.press("down",5,0.3)
pyautogui.press("enter",1,1)

print("Entering shop information")
pyautogui.press(['alt','e'],1,2)
pyautogui.press("down",6,0.3)
pyautogui.press("enter",1,1)
pyautogui.press("Tab",7,0.7)
pyautogui.press("enter",1,0.3)

print("Invoking SalesMate+ File Root Menu")
pyautogui.press(['alt','f'],1,2)

print("Press b to invoke Backup Folder Dialog")
pyautogui.press("b",1,1.5
)

print("Directing Automation to Krishna Drive")
pyautogui.press("k",1,1)

print("Now press Right arrow Key to Expand the Tree")
pyautogui.press("right",1,2.0)

print("Directing to to SMP Folder")
pyautogui.typewrite("SMP")

print("Press Enter Key to Backuup Data")
pyautogui.press("enter",1,2.0)

print("Press Enter Again to Close the OK Button")
pyautogui.press("enter")

print("Adding a new Customer")
pyautogui.press(['alt','c'],1,1)

print("Invoking new customer details menu")
pyautogui.press('a',1,1)

print("Press alt to select next entry")
pyautogui.press("Tab",2,1)

print("Enter First Name")
pyautogui.typewrite("Krishna",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Last Name")
pyautogui.typewrite("Panchal",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Title")
pyautogui.typewrite("Ms",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Address")
pyautogui.typewrite("Maharashtra,India",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Phone Number")
pyautogui.typewrite("9067244023",0.1)

print("Press alt to select next entry")
pyautogui.press("Tab",1,1)

print("Enter Email Id")
pyautogui.typewrite("mekrish1002@gmail.com",0.1)

print("To Select Customer Image")
pyautogui.press("Tab",1,1)
pyautogui.press("Space",1,1)
pyautogui.typewrite("SMPBanner.bmp",0.2)
pyautogui.press("enter",1,1)

print("Press tab to select next entry")
pyautogui.press("Tab",2,1)

print("Choosing Retail Category")
pyautogui.typewrite("Retail ")

print("Press enter to select next entry")
pyautogui.press("enter",1,1)

print("Enter Comment")
pyautogui.typewrite("KTS Infotech")

print("Press enter to select next entry")
pyautogui.press("enter",2,1)

print("Enter membership fees")
pyautogui.press("Space",1,1)
pyautogui.press("Tab",1,1)
pyautogui.typewrite("200",0.1)

print("Enter Security Deposit")
pyautogui.press("Tab",1,1)
pyautogui.press("Space",1,1)
pyautogui.press("Tab",1,1)
pyautogui.typewrite("1000",0.1)

print("Saving Info")
pyautogui.press("Tab",1,1)
pyautogui.press("enter",2,1)



