def calender():
 import calendar
 year = int(input('enter year:'))
 month = int(input('enter month:'))
 print("\n",calendar.month(year,month))
calender()
def continue_():
  n=str(input('do you want to be continue(yes/no):'))
  if n=="yes":
     calender()
     continue_()
  elif n=='no':
     print('exiting.......')
  else:
     print('you entered invalid option:')
     calender()
     continue_()
continue_() 