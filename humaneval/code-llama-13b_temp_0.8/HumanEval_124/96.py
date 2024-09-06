
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
    # Get the day, month and year from the date string
    day, month, year = date.split("-")

    if len(day) == 0 or len(month) == 0 or len(year) == 0:
        return False

    # Convert strings to int
    day = int(day)
    month = int(month)
    year = int(year)

    # Month 1, 3, 5, 7, 8, 10, 12
    if month in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= day <= 31:
            return True
        else:
            return False

    # Month 4, 6, 9, 11
    if month in (4, 6, 9, 11):
        if 1 <= day <= 30:
            return True
        else:
            return False

    # Month 2
    if month == 2:
        # Leap Year
        if year % 4 == 0:
            if 1 <= day <= 29:
                return True
            else:
                return False
        # Not Leap Year
        else:
            if 1 <= day <= 28:
                return True
            else:
                return False

    # Month is not between 1 and 12
    if month < 1 or month > 12:
        return False

    return False
