
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    try:
        year,month,day = date.split('-')
        year,month,day = int(year),int(month),int(day)
        if month in [1,3,5,7,8,10,12]:
            return 1<=day<=31 and 1<=month<=12 and 2000<=year<=3000
        elif month in [4,6,9,11]:
            return 1<=day<=30 and 1<=month<=12 and 2000<=year<=3000
        elif month == 2:
            return (year%4==0 and year%100!=0) or year%400==0 and 1<=day<=29 and 1<=month<=12 and 2000<=year<=3000
    except:
        return False
