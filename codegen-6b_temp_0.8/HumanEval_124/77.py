
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
    day_regex = re.compile(r'^\d{1,2}$')
    month_regex = re.compile(r'^\d{1,2}(\/|-){1}(\d{1,2}){2}$')
    date_regex = re.compile(r'^(\d{1,2})(\/|-){1}(\d{1,2}){2}$')

    if not date:
        return False

    if not day_regex.match(date[0]):
        return False

    if not month_regex.match(date[1]):
        return False

    if not date_regex.match(date[2]):
        return False

    month = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
             '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    if int(date[2]) % 4 == 0 and month.get(date[1]):
        month[date[1]] += 1

    if int(date[0]) > 12 or int(date[0]) < 1:
        return False
    if int(date[1]) > 12 or int(date[1]) < 1:
        return False
    if int(date[2]) > 2015 or int(date[2]) < 1000:
        return False

    return True
