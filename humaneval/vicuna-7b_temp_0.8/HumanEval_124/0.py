
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
    d = datetime.strptime(date, "%m-%d-%Y")
    if date.strip() == "":
        return False
    if d.year < 1 or d.year > 9999 or d.month < 1 or d.month > 12 or d.day < 1 or d.day > 31 or (d.month == 2 and d.day > 28 or (d.month == 4 and d.day > 30) or (d.month == 6 and d.day > 30) or (d.month == 9 and d.day > 30) or (d.month == 11 and d.day > 30) or d.day < 1 or d.day > 31):
        return False
    return True
