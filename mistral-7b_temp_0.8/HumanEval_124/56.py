
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
    day = date[5:7]
    month = date[0:2]
    year = date[8:10]
    if len(date) == 10:
        if day.isdigit() and month.isdigit() and year.isdigit():
            month = int(month)
            year = int(year)
            if month > 12:
                return False
            elif month < 1:
                return False
            elif year < 1900:
                return False
            elif year > 9999:
                return False
            elif day.isdigit():
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    if int(day) > 31:
                        return False
                    elif int(day) < 1:
                        return False
                    else:
                        return True
                elif month == 4 or month == 6 or month == 9 or month ==
