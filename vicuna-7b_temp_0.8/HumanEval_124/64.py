
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
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    if len(date) != 10:
        return False
    elif (day < 1 or day > 31) and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return False
    elif (day < 1 or day > 30) and (month == 4 or month == 6 or month == 9 or month == 11):
        return False
    elif (day < 1 or day > 29) and month == 2:
        return False
    else:
        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 1900 and year <= 9999:
            return True
        else:
            return False
