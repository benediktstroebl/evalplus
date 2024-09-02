
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
    if date == "":
        return False

    date_split = date.split("-")

    month_int = int(date_split[0])
    day_int = int(date_split[1])
    year_int = int(date_split[2])

    if month_int < 1 or month_int > 12:
        return False

    if month_int == 2:
        if year_int % 400 == 0 or (year_int % 4 == 0 and year_int % 100 != 0):
            if day_int < 1 or day_int > 29:
                return False
        else:
            if day_int < 1 or day_int > 28:
                return False
    elif month_int in [1, 3, 5, 7, 8, 10, 12]:
        if day_int < 1 or day_int > 31:
            return False
    elif month_int in [4, 6, 9, 
