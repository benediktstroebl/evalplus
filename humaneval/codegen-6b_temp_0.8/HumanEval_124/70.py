
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
    valid_date = False

    # check if date is empty string
    if not date:
        return valid_date

    # check if date of the form mm-dd-yyyy
    date_regex = r'^(0?([1-9]|1[0-2])(-0?[1-9]|[1-2][0-9]|3[01]))-((0?[1-9]|[1-2][0-9]|30|31))-((20)?[0-9]{2})$'
    if re.match(date_regex, date):
        valid_date = True

    # check if date is valid
    if valid_date:
        y, m, d = date.split('-')
        if not int(y) == 0:
            # check if year is valid
            if not (int(y) >= -1):
                valid_date = False

            # check if month is valid
            if not (int(m) < 1 or int(m) > 12):
                valid_date = False

            # check if day is valid
            if not (int(d) < 1 or int(d) > 31):
                valid_date = False
        else:
            # check if month is valid
            if not (int(m) < 1 or int(m) > 12):
                valid_date = False

            # check if day is valid
            if not (int(d) < 1 or int(d) > 30):
                valid_date = False

    return valid_date

