'''
requirements:
allow user to enter date and time in any format you pick
validate the date and time
make sure year is between 1900 and 2020
print date time in yyy-mm-dd hh:mm:ss format and unix time
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

