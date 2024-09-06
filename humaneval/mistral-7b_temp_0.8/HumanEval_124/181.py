
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
    def month_days(month):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 2:
            return 29


    if date == '' or date == ' ':
        return False

    if len(date) == 10 and date[2] == '-' and date[5] == '-':
        try:
            month = int(date[0:2])
            day = int(date[3:5])
            year = int(date[6:10])
        except ValueError:
            return False

        if year > 0 and year < 100:
            if month > 0 and month < 13:
                if day > 0 and day < month_days(month) + 1:
                    return True

    return False
