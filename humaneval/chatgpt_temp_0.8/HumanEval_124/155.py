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
    # Check if date is empty
    if not date:
        return False
    
    # Check if date is in correct format
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    
    # Extract month, day, and year from date
    month, day, year = map(int, date.split('-'))
    
    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False
    
    # Check number of days based on month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month == 2:
        # Check for leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = 30
    
    if day < 1 or day > max_days:
        return False
    
    return True
