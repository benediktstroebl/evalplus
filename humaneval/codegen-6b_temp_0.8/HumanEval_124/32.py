
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
    p = re.match(r'^(1[012]|0[1-9]|[12]0),?\s?(0[1-9]|1[012])\s?,?([1-2][0-9][0-9][0-9]{3})$', date)
    months = {'1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09',
              '10': '10', '11': '11', '12': '12'}
    days = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
            '11': 30, '12': 31}
    if p:
        if int(p.group(3)) < 1 or int(p.group(3)) > 31:
            return False
        if int(p.group(2)) > 12:
            return False
        if int(p.group(2)) == 2 and int(p.group(1)) > 28:
            return False
        if int(p.group(2)) == 2 and int(p.group(1)) == 2 and int(p.group(3)) < 1:
            return False
        if int(p.group(2)) == 2 and int(p.group(1)) == 2 and int(p.group(3)) > 29:
            return False
        for i in months:
            if i == p.group(2):
                for j in days:
                    if int(p.group(1)) == int(i) and int(p.group(3)) == int(j):
                        return True
    return False

