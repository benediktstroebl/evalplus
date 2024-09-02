
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

    try:
        # Check month
        m = int(date[0:2])
        # Check day
        d = int(date[3:5])
        # Check year
        y = int(date[6:10])
    except:
        return False

    if y < 1 or y > 9999:
        return False

    if m < 1 or m > 12:
        return False

    if d < 1 or d > 31:
        if m == 2:
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                if d > 29:
                    return False
            else:
                if d > 28:
                    return False
        elif m in [4, 6, 9, 11]:
            if d > 30:
                return False

    return True

