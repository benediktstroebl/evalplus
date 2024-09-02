
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
    if not date:
        return False

    num_days = 0
    date_valid = True
    date = date.split('-')
    if len(date) != 3:
        return False

    # month check
    month = date[0].strip().capitalize()
    if int(month) < 1 or int(month) > 12:
        return False

    # year check
    year = date[2]
    try:
        int(year)
    except ValueError:
        return False

    # day check
    day = date[1].strip()
    if day == "":
        return False
    try:
        int(day)
    except ValueError:
        return False
    num_days += int(day)

    # month 30 check
    if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30:
            return False
    # month 31 check
    elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 31:
            return False

    # day less than 1 check
    if int(day) < 1:
        return False

    return date_valid

