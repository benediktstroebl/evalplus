
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

    if date.isdigit() == False:
        return False
    date = date.split('-')
    month = date[0]
    day = date[1]
    year = date[2]
    if (month.isdigit() == False or day.isdigit() == False or year.isdigit() == False):
        return False
    month = int(month)
    day = int(day)
    year = int(year)

    if (month > 12 or month < 1):
        return False
    if (day > 31 or day < 1):
        return False
    if (month == 2):
        if (day > 29 or day < 1):
            return False
    if (month == 4 or month == 6 or month == 9 or month == 11):
        if (day > 30 or day < 1):
            return False
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
