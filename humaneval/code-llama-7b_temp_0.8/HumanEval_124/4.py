
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
    # write your code here
    # return True or False
    if date == '':
        return False
    m = int(date.split('-')[0])
    d = int(date.split('-')[1])
    y = int(date.split('-')[2])
    if m < 1 or m > 12:
        return False
    if y < 2021 or y > 2050:
        return False
    if d < 1 or d > 31:
        return False
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d < 1 or d > 31:
            return False
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d < 1 or d > 30:
            return False
    if m == 2:
        if d < 1 or d > 29:
            return False
    return True
