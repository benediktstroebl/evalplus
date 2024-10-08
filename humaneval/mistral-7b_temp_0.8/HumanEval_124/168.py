
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

    date_parts = date.split("-")

    if len(date_parts) != 3 or len(date_parts[0]) != 2 or len(date_parts[1]) != 2 or len(date_parts[2]) != 4:
        return False

    # Month
    if 1 <= int(date_parts[0]) <= 12:
        pass
    else:
        return False

    # Day
    if int(date_parts[1]) > 28:
        if int(date_parts[0]) == 2:
            return False
        elif int(date_parts[0]) in [4, 6, 9, 11]:
            return False
        else:
            return True
    elif int(date_parts[1]) <= 0:
        return False
    else:
        return True

    # Year
    if int(date_parts[2]) > 9999:
        return False
    elif int(date_parts[2]) < 
