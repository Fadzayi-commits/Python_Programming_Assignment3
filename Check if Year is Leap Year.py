import calendar

c_year = int(input("Enter year:"))
year = c_year
leap = year % 4 == 0 and year %100 != 0

if leap:
   print("It's a leap year")

else:
    print("It's not a leap year")
