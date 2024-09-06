
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
    d = date.split("-")
    if len(d) == 1:
        return False
    if len(d) == 2:
        if len(d[1]) < 1 or len(d[1]) > 31:
            return False
        if d[0] < '1' or d[0] > '12':
            return False
    if len(d) == 3:
        if d[0] < '1' or d[0] > '12':
            return False
        if d[1] < '1' or d[1] > '12':
            return False
    if d[2] < '1' or d[2] > '31':
        return False
    if d[0] >= '01' and d[0] <= '31':
        if d[1] >= '01' and d[1] <= '31':
            if d[2] >= '01' and d[2] <= '31':
                return True
            else:
                return False
    else:
        return False