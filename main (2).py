# Write a program that determines whether a year entered by the user in a leap year or not using if_elif_else statement           
def isleapYear(year):
  if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return False
    Year = int(input("Enter a year: "))
    if isLeapYear(year):
      print('{} is a leap year.'.format(year))
    else:
      print('{} is not a leap year.'.format(year))