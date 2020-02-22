
import time
from datetime import date
import datetime
import calendar 


today = date.today()
print("today's date is :", today)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("time now is " ,current_time)


date= input("Enter date in DD/MM/YYYY format :")
date1= time.strptime(date ,"%d/%m/%Y")
                     
seconds= time.mktime(t) - time.mktime(date1)
print("Difference in seconds :" ,seconds)


hours = seconds // 3600
print("Difference in hours :" , hours)

days = hours // 24
print ("Difference in days :" , days)

year = int(time.strftime("%Y", date1))
month = int(time.strftime("%m", date1))
print  ("Days in month:", calendar.monthrange(year,month)[1])

