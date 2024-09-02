
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

    import re

    months = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days = [1, 30, 31, 28, 29, 30, 31, 30, 31, 30, 31, 30, 31]
    if date == '':
        return False
    elif re.search('^[0-9]{2}-[0-9]{2}-[0-9]{4}$', date) == None:
        return False
    else:
        day, month, year = date.split('-')
        month = int(month)
        year = int(year)
        day = int(day)
        if month < 1 or month > 12:
            return False
        else:
            if day < 1 or day > days[month-1]:
                return False
            else:
                if month in days_30:
                    if day < 1 or day > 30:
                        return False
                if month in days_31:
                    if day < 1 or day > 31:
                        return False
                if month == 2:
                    if year % 400 == 0:
                        if day < 1 or day > 29:
                            return False
                    if year % 4 == 0:
                        if day < 1 or day > 29:
                            return False
                    if year % 100 == 0:
                        if day < 1 or day > 28:
                            return False
                    if day < 1 or day > 28:
                        return False
    return True
    
