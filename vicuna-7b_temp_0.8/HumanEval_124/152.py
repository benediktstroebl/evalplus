
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
    if len(date) == 0:
        return False
    
    month, day, year = map(int, date.split("/"))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 31:
                return False
            elif day <= 30:
                return True
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
            elif day <= 29:
                return True
    return True

test = [
    ['01-01-1900', True],
    ['12-12-1999', True],
    ['12-31-1999', True],
    ['01-01-2000', True],
    ['02-01-2000', False],
    ['03-01-2000', False],
    ['04-01-2000', False],
    ['05-01-2000', False],
    ['06-01-2000', False],
    ['07-01-2000', False],
    ['08-01-2000', False],
    ['09-01-2000', False],
    ['10-01-2000', False],
    ['11-01-2000', False],
    ['12-01-2000', False],
    ['01-13-2000', False],
    ['02-14-2000', False],
    ['03-15-2000', False],
    ['04-16-2000', False],
    ['05-17-2000', False],
    ['06-18-2000', False],
    ['0
