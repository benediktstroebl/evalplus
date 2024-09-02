
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
    # we make sure that the input is a string
    if not isinstance(date, str):
        return False

    # we split the string into three parts: month, day, and year
    parts = date.split('-')

    # make sure the parts are exactly three
    if len(parts) != 3:
        return False

    # make sure that each part is a number
    for part in parts:
        try:
            int(part)
        except:
            return False

    # make sure that the month is a valid one
    if int(parts[0]) < 1 or int(parts[0]) > 12:
        return False

    # make sure that the day is a valid one
    if int(parts[0]) == 2:
        if int(parts[1]) < 1 or int(parts[1]) > 29:
            return False
    elif int(parts[0]) % 2 != 0:
        if int(parts[1]) < 1 or int(parts[1]) > 31:
            return False
    else:
        if int(parts[1]) < 1 or int(parts[1]) > 30:
            return False

    # make sure that the year is a valid one
    if int(parts[2]) < 2019 or int(parts[2]) > 2100:
        return False

    return True

