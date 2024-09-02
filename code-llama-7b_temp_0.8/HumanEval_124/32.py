
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
    import datetime
    import calendar

    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:])

    valid_month = False
    valid_day = False
    valid_year = False

    if 0 < month < 13:
        valid_month = True

    if 0 < day < 32:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 0 and day < 31:
                valid_day = True
        elif month in [4, 6, 9, 11]:
            if day > 0 and day < 31:
                valid_day = True
        elif month == 2:
            if day > 0 and day < 29:
                valid_day = True

    if year > 1900 and year < datetime.datetime.now().year + 1:
        valid_year = True

    return valid_month and valid_day and valid_year and len(date) == 10
