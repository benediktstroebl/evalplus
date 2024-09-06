
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

    date = date.split('-')
    if len(date)!= 3:
        return False
    
    month, day, year = date
    if len(month)!= 2 or len(day)!= 2 or len(year)!= 4:
        return False
    if month[0] not in '0123456789' or month[1] not in '0123456789' or day[0] not in '0123456789' or day[1] not in '0123456789':
        return False
    
    if (month[0] in '01' and day[0] in '01' and year[0] in '01') or (month[0] in '4' and day[0] in '01' and year[0] in '01'): # months 1,3,5,7,8,10,12
        if int(month) < 1 or int(month) > 12:
            return False
    if (month[0] in '4' and day[0] in '01' and year[0] in '01') or (month[0
