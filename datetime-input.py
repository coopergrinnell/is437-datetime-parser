'''
requirements:
allow user to enter date and time in any format you pick
validate the date and time
make sure year is between 1900 and 2020
print date time in yyy-mm-dd hh:mm:ss format and unix time
'''

from datetime import datetime

year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0

while 1:
    year = input("enter year as YYYY: ")
    if int(year) >= 1900 and int(year) <= 2020:
        print('good')
    else:
        print('bad')
        break
    
    month = input("enter month as MM: ")
    if int(month) >= 1 and int(month) <= 12:
        print('good')
    else:
        print('bad')
        break
    
    day = input("enter day as DD: ")
    if int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if int(day) >= 1 and int(day) <= 31:
            print('good 31')
        else:
            print('bad 31')
            break
    if int(month) == 4 or 6 or 9 or 11:
        if int(day) >= 1 and int(day) <= 30:
            print('good 30')
        else:
            print('bad 30')
            break
    if int(month) == 2:
        if int(year) % 4 == 0:
            if int(day) >= 1 and int(day) <= 29:
                print('good 29')
            else:
                print('bad')
                break
        if int(day) >= 1 and int(day) <= 28:
            print('good 28')
        else:
            print('bad')
            break
    else:
        print('bad')
        break
    
    hour = input("enter hour as HH in 24 hour format: ")
    if int(hour) >= 1 and int(hour) <= 24:
        print('good')
    else:
        print('bad')
        break
    minute = input("enter minute as MM: ")
    if int(minute) >= 1 and int(minute) <= 60:
        print('good')
    else:
        print('bad')
        break

    second = input("enter seconds as SS: ")
    if int(second) >= 1 and int(second) <= 60:
        print('good')
    else:
        print('bad')
        break

    print(str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second))
    break