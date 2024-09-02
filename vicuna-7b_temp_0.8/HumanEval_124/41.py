
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
    # Regular expression to validate date format
    pattern = re.compile(r'^(?:0?[1-9]|1[012])[- \\.](?:(?:0?[13578]|1[02])[- \\.](?:(?:(?:[1]|[2-9])\d\d|0[1-9]|1[012])[- \\.](?:(?:19|20)\d\d)|(?:2000|20[012])\\-(?:0[1-9]|1[012])[- \\.]\\d\d\d\d)$')

    # if date is empty or invalid
    if not date:
        return False

    # Convert date to datetime object
    dt = datetime.strptime(date, '%m-%d-%Y')

    # Check if the number of days is valid
    if dt.day < 1 or dt.day > 31 and dt.month in [1, 3, 5, 7, 8, 10, 12] or dt.day < 1 or dt.day > 30 and dt.month in [4, 6, 9, 11] or dt.day < 1 or dt.day > 29 and dt.month == 2:
        return False

    # Check if the month is valid
    if dt.month < 1 or dt.month > 12:
        return False

    # Check if the date is valid
    if dt.year < 1900 or dt.year > 2020 or dt.month == 2 and dt.day > 28 or dt.day == 29:
        return False

    # Check if the date is in the format mm-dd-yyyy
    if dt.strftime('%m-%d-%Y') != date:
        return False

    return True