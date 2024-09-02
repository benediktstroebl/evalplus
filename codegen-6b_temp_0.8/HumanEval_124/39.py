
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
    import re
    regex = re.compile(r'^(01|02|03|04|05|06|07|08|09|10|11|12)$')
    regex_m = re.compile(r'^(01|02|03|04|05|06|07|08|09|10|11|12|01|02|03|04|05|06|07|08|09|10|11|12)')
    regex_date = re.compile(r'^([01]{1}|[12]{1})[-/]([0]{1}|[1-9]{1,2})[-/]([0-9]{4})$')
    valid_date = [regex.match(date), regex_m.match(date), regex_date.match(date)]
    return False not in valid_date

assert(valid_date('01-01-2010') == False)
assert(valid_date('01-01-2010') == False)
assert(valid_date('02-01-2010') == False)
assert(valid_date('03-01-2010') == False)
assert(valid_date('03-01-2010') == False)
assert(valid_date('01-01-0110') == False)
assert(valid_date('01-01-0110') == False)
assert(valid_date('02-01-0110') == False)
assert(valid_date('03-01-0110') == False)
assert(valid_date('04-01-0110') == False)
assert(valid_date('05-01-0110') == False)
assert(valid_date('06-01-0110') == False)
assert(valid_date('07-01-0110') == False)
assert(valid_date('08-01-0110') == False)
assert(valid_date('09-01-0110') == False)
assert(valid_date('10-01-0110') == False)
assert(valid_date('11-01-0110') == False)
assert(valid_date('12-01-0110') == False)