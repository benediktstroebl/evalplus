
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
    if len(date) < 1:
        return False
    month, day, year = [int(x) for x in date.split('-')]
    month_dict = {1: (1, 31), 2: (2, 28), 3: (3, 31), 4: (4, 30), 5: (5, 31), 6: (6, 30), 7: (7, 31), 8: (8, 31), 9: (9, 30), 10: (10, 31), 11: (11, 30), 12: (12, 31)}
    if month < 1 or month > 12:
        return False
    if month in month_dict:
        if day < 1 or day > month_dict[month][1]:
            return False
    if year < 1900 or year > 2020:
        return False
    if month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True
