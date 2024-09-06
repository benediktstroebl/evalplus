
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

    days_in_month = {
        '01': 31,
        '02': 29,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    # 1. The date string is not empty.
    if date == '':
        return False

    # 2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    month, day, year = date.split('-')

    if month == '02' and int(day) > 29:
        return False

    if month != '02' and int(day) > days_in_month[month]:
        return False

    # 3. The months should not be less than 1 or higher than 12.
    if int(month) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return False

    # 4. The date should be in the format: mm-dd-yyyy
    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False

    return True
