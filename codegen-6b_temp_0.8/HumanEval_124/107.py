
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
    days_in_month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if len(date) == 0:
        return False
    date = date.split("-")
    if len(date) != 3:
        return False
    try:
        d, m, y = [int(d) for d in date]
    except ValueError:
        return False
    if d < 1 or d > 31:
        return False
    if m < 1 or m > 12:
        return False
    if (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        return False
    if (m == 2) and d > 29:
        return False
    if m in days_in_month:
        if d in range(1, days_in_month[m] + 1):
            return True
        else:
            return False
    elif m in month_days:
        if d in range(1, month_days[m] + 1):
            return True
        else:
            return False
    else:
        raise ValueError
