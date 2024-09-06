
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
    valid_months = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    year, month, day = date.split('-')
    a = int(year)
    b = int(month)
    c = int(day)
    if c < 1 or c > 31:
        return False
    if b < 1 or b > 12:
        return False
    if a < 1 or a > 9999:
        return False
    if b == 2:
        if c < 1 or c > valid_months[month]:
            return False
    elif b > 2:
        if c < 1 or c > valid_months[month]:
            return False
    else:
        if c < 1 or c > valid_months[month]:
            return False
    return True
