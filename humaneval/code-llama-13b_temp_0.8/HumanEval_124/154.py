
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
    months = ['01', '03', '05', '07', '08', '10', '12']
    correct_days = {'01': 31, '03': 31, '05': 31, '07': 31, '08': 31, '10': 31, '12': 31}
    months2 = ['04', '06', '09', '11']
    correct_days2 = {'04': 30, '06': 30, '09': 30, '11': 30}
    months3 = ['02']
    correct_days3 = {'02': 28}

    if len(date) == 0:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if date[0:2] not in months and date[0:2] not in months2 and date[0:2] not in months3:
        return False
    if date[3:5] > correct_days[date[0:2]] or date[3:5] == '00':
        return False
    if date[0:2] in months2 and date[3:5] > correct_days2[date[0:2]]:
        return False
    if date[0:2] in months3 and date[3:5] > correct_days3[date[0:2]]:
        return False

    return True

