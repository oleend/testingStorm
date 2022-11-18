import math
import time
from datetime import datetime
from ImportingThings import TimeMaster

#This is for the stopwatch
instancetime = datetime.now()
appTime = True

print('-----Clock Application-----')

app = True

while app == True:
   currentTime = datetime.now()
   called_Time = currentTime.strftime("%H:%M:%S")
   print('Current Time is: ' + called_Time)
   clockOption = input("What would you like to do: Refresh (T)ime, Show (D)ate, (S)topwatch, (Q)uit, Summon TimeLord(W): ").lower()
   print()

   if clockOption  == 'q':
        app = False

   if clockOption == 't':
        continue

#Imports the TimeLord
   if clockOption == 'w':
       TimeLord = TimeMaster()
       print("The Time Lord Master was summoned, and used his dark magic to send you to his time.")
       Hour = round(TimeLord.time_magic() * float(currentTime.strftime('%H')))
       Minute = round(TimeLord.time_magic() * float(currentTime.strftime('%M')))
       Second = round(TimeLord.time_magic() * float(currentTime.strftime('%S')))
       called_Time = Hour + Minute + Second
       print(f"The current time is: {Hour}:{Minute}:{Second}, Good Luck!" )
       time.sleep(5)
       print()
       print("You found a way back to reality!")
   if clockOption == 'd':
       currentTime = datetime.now()
       called_date = currentTime.strftime("%m/%d/%Y")
       print("Today is: " + called_date)
       input("Press any key to return to main menu...")
       print()

   if clockOption == 's':
        print()

        #This is if the stopwatch is first called
        if appTime == True:
            print('-----Stopwatch Application-----')
            print('*If you use this for over an hour, it will not run correctly*')
            print()

            instanceStopwatch = datetime.now()
            start = instanceStopwatch.strftime("%M.%S")
            end = instancetime.strftime('%M.%S')
            start = float(start)
            end = float(end)

            stopwatch = round((start - end),2)
            print(f'it has been {stopwatch} minutes since the application started')

            print('Would you like to reset the Stopwatch? (Y)es or (R)eturn to Main Menu')

            reset = input().lower()

            if reset == 'y':
                instancetime = datetime.now()
                print('Stopwatch reset')
                appTime = False
                stopwatchCheck = True
            if reset == 'r':
                print()
            else:
                if appTime == True:
                    print('That is not a valid option.')


            input("Press any key...")
            print()

        if appTime == False:
            print('-----Stopwatch Application-----')
            print('*If you use this for over an hour, it will not run correctly*')
            print()

            instanceStopwatch = datetime.now()
            start = instanceStopwatch.strftime("%M.%S")
            end = instancetime.strftime('%M.%S')
            start = float(start)
            end = float(end)

            stopwatch = round((start - end),2)
            print(f'it has been {stopwatch} minutes since the Stopwatch Started')

            print('What would you like to do? (R)eset AND (R)eturn to the MAIN MENU OR ANY KEY to return to MAIN MENU ')

            reset = input().lower()

            if reset == 'r':
                instancetime = datetime.now()
                print('Stopwatch reset')
                print()
                appTime = False
            else:
                print()

   else:
       if app == True:
        print("Make sure to Enter a Valid Option! Clock Updated and Returned.")
       print()



#On the call of this this will display the time
#Should I put an alarm on or not. function for that

