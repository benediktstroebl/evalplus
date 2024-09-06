
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

    try:
        date = date.split('-')
        date_month, date_day, date_year = date[0], date[1], date[2]
        date_month = int(date_month)
        date_day = int(date_day)
        date_year = int(date_year)
        if (date_month > 12 or date_month < 1):
            return False
        if (date_month in [1,3,5,7,8,10,12] and date_day > 31):
            return False
        if (date_month in [4,6,9,11] and date_day > 30):
            return False
        if (date_month == 2 and date_day > 29):
            return False
        if (date_month == 2 and date_day < 1):
            return False
        if (date_month == 4 and date_day > 31):
            return False
        if (date_month == 6 and date_day > 30):
            return False
        if (date_month == 9 and date_day > 30):
            return
