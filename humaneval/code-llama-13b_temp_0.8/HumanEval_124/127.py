
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
    # Write your code here

    # split the date string into month day and year
    # split date into month, day, year
    # find out if the month is in the range of 1-12
    # if month is 3, 6, 9, 11, find out if the day is in the range of 1-30
    # if month is 1, 4, 7, 8, 10, 12, find out if the day is in the range of 1-31
    # if month is 2, find out if the day is in the range of 1-29
    # lastly, if the date is formatted as mm-dd-yyyy, it is a valid date
    # the day and year can be any number, so find the first - to find the end of the month

    if date == '':
        return False

    month = date[0:date.find('-')]

    day = date[date.find('-') + 1:date.find('-', date.find('-') + 1)]

    year = date[date.find('-', date.find('-') + 1) + 1:]

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        return False

    if month in [3, 6, 9, 11]:
        if day < 1 or day > 30:
            return False

    if month in [1, 4, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False

    if month == 2:
        if day < 1 or day > 29:
            return False

    if date[-5:date.find('-')] == '-':
        return True
    else:
        return False

