
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
    # your code here
    # Number of days in months
    day_dict = {'Jan': 31,
                'Feb': 28,
                'Mar': 31,
                'Apr': 30,
                'May': 31,
                'Jun': 30,
                'Jul': 31,
                'Aug': 31,
                'Sep': 30,
                'Oct': 31,
                'Nov': 30,
                'Dec': 31}

    # Check each pair and return False if invalid date
    if not len(date):
        return False

    if not '-' in date:
        return False
    
    dt_in = date.split('-')

    if len(dt_in) != 3 and len(dt_in) != 4:
        return False

    if len(dt_in) == 3:
        if not dt_in[2].isdigit():
            return False
        if int(dt_in[2]) > 3000:
            return False
        return True
    
    if len(dt_in) == 4:
        if not dt_in[0].isdigit():
            return False
        if not dt_in[1].isdigit():
            return False
        if not dt_in[2].isdigit():
            return False
        return True
    return False

