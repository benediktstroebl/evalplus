
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
    # Extract the month, day, and year from the date string
    month, day, year = map(int, date.split('-')[1:3])

    # Calculate the number of days in the month
    max_days = {
        1: 31,
        3: 31,
        5: 30,
        7: 31,
        8: 31,
        10: 30,
        12: 31
    }.get(month, 30)
    if day > max_days:
        return False

    # Check if the day is valid
    if month < 1 or month > 12 or day < 1 or day > max_days:
        return False

    # Format the date string in the expected format
    expected_date = '{}{}-{}-{}.'.format(month, day, year)
    if expected_date != date:
        return False

    return True