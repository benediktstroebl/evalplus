
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

    # check if date is empty
    if not date:
        return False

    # split date into different parts
    date_split = date.split('-')

    # check if date has three parts
    if len(date_split) != 3:
        return False

    # check if month, day, and year are numbers
    for i in date_split:
        if not i.isdigit():
            return False

    # convert strings to ints
    month = int(date_split[0])
    day = int(date_split[1])
    year = int(date_split[2])

    # check if month is in range 1-12
    if month > 12 or month < 1:
        return False

    # check if day is valid for month
    if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
        return False
    if month in [4,6,9,11] and day < 1 or day > 30:
        return False
    if month == 2 and day < 1 or day > 29:
        return False

    # check if year is valid
    if year > 2019 or year < 1900:
        return False

    return True
