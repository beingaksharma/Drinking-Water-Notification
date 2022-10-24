import time
from plyer import notification

if __name__ == "__main__":
   while True:
        notification.notify(
            title="Please Drink Water!",
            message="On a regular basis, human body needs 2 to 2.5 liters of water. It is important to note in this regard that food items with enriched moisture also add to the body’s need for water. Thus consumption of food item leads to the intake of 1 liter of water.",
            app_icon="D:\A DRIVE\PROJECTS\PYTHON PROJECTS\Water.ico",  #icon reflect when we execute this program
            timeout = 10
            )

time.sleep(60)   # time in second time.speed(60*60)
 
#to run in background type : pythonw .\DrinkWaterNotification.py in terminal

