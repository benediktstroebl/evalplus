
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
    # Check if the date string is empty or not
    if len(date) == 0:
        return False

    # Split the date string into year, month and day
    year, month, day = map(int, date.split('/'))

    # Check if the month is valid
    if 1 <= month <= 12:
        if month < 1 or month > 12:
            return False

    # Check if the day is valid
    if day < 1 or day > 31:
        if day < 1 or (day == 1 and month in [4,6,9,11]) or (day == 29 and month in [2]) or (day > 31):
            return False

    # Check if the year is valid
    if year < 1000 or year > 9999:
        return False

    # If all the above conditions are satisfied, the date is valid
    return True