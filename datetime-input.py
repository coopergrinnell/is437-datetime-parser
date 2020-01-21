'''
requirements:
allow user to enter date and time in any format you pick
validate the date and time
make sure year is between 1900 and 2020
print date time in yyy-mm-dd hh:mm:ss format and unix time
'''

'''
year = input("enter year: ")
#must be between 1900 - 2020
yeari = None
try:
    yeari = int(year)
except:
    pass
if yeari is not None:

    if yeari >= 1900:
        if yeari <= 2020:
            print(str(yeari) + " is valid :)")
        else:
            print("year too big")
    else:
        print("year too small")
else:
    print(str(year) + " is not valid")
'''

from datetime import datetime

year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0


year = input("enter year: ")
yeari = None
try:
    yeari = int(year)
except:
    pass
if yeari is not None:

    if yeari >= 1900:
        if yeari <= 2020:
            print(str(yeari) + " is valid :)")
            year = yeari
            #print(year)
        else:
            print("year too big")
    else:
        print("year too small")
else:
    print(str(year) + " is not valid")

month = input("enter month as a number: ")
monthi = None
try:
    monthi = int(month)
except:
    pass
if monthi is not None:

    if monthi >= 1:
        if monthi <= 12:
            print(str(monthi) + " is valid :)")
            month = monthi
            #print(year)
        else:
            print("month too big")
    else:
        print("month too small")
else:
    print(str(month) + " is not valid")

day = input("enter day: ")
dayi = None
try:
    dayi = int(day)
except:
    pass
if dayi is not None:
    if month = 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if dayi >= 1:
            if dayi <= 31:
                print(str(dayi) + " is valid :)")
                day = dayi
                #print(year)
            else:
                print("day too big")
        else:
            print("day too small")
    else:
        print(str(day) + " is not valid")
    
    elif month = 4 or 6 or 9 or 11:
        if dayi >= 1:
            if dayi <= 31:
                print(str(dayi) + " is valid :)")
                day = dayi
                #print(year)
            else:
                print("day too big")
        else:
            print("day too small")
    else:
        print(str(day) + " is not valid")

hour = input("enter hour: ")
minute = input("enter minute: ")
second = input("enter second: ")