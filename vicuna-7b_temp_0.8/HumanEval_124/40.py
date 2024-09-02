
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
    try:
        date = date.strip()
        if len(date) < 1 or len(date) > 31:
            return False
        if date[:2] not in ['01', '03', '05', '07', '08', '10', '12']:
            return False
        if date[:2] == '02' and len(date) < 29:
            return False
        if date[2:4] not in ['01', '03', '05', '07', '09', '11', '12']:
            return False
        month, day, year = map(int, date.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 1000 or year > 9999:
            return False
        return True

    except Exception as e:
        return False

valid_date_test = [
    ("01-01-1990", True),
    ("12-31-1999", True),
    ("12-31-1999", True),
    ("12-31-2010", True),
    ("01-02-2020", False),
    ("02-03-2013", False),
    ("03-01-2012", False),
    ("04-0-2040", False),
    ("06-04-2020", True),
    ("06/04/2020", False),
    ("07-12-2011", False),
    ("09-30-2013", False),
    ("12-28-2012", False),
    ("29-12-2011", False),
    ("01-13-2013", False),
    ("02-28-2013", False),
    ("03-31-
