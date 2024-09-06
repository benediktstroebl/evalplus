
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

    if not date:
        return False

    # Splits the date into mm, dd, yyyy
    # and converts them to integers
    mm, dd, yyyy = list(map(int, date.split('-')))

    if mm < 1 or mm > 12:
        return False
    
    # months with 30 days
    if (mm == 4 or mm == 6 or mm == 9 or mm == 11) and (dd < 1 or dd > 30):
        return False

    # months with 31 days
    if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and (dd < 1 or dd > 31):
        return False

    # February month with 28 or 29 days
    if mm == 2 and (dd < 1 or dd > 29):
        return False

    return True
