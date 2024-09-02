
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
    # Regular expression to check if date string is in format of mm-dd-yyyy
    reg_exp = re.compile(r'^([0-3]?[0-9])([0-1]?[0-9])([0-3]?[0-9])([1357920000000]|[2469])')

    # Extract month, day and year from the date string
    match = re.search(reg_exp, date)
    if match:
        month, day, year = match.groups()

        # check if the month is in valid range
        if 1 <= month <= 12:
            if len(str(day)) <= 30:
                if year < 2000 or year >= 2040:
                    return True
            elif len(str(day)) <= 31:
                if year < 2012 or year >= 2020:
                    return True
        else:
            if len(str(day)) <= 30:
                return True

    return False