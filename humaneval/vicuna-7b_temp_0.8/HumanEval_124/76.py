
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
    if len(date) == 0:
        return False
    if date[:2] not in ['01', '03', '05', '07', '08', '10', '12']:
        return False
    if date[:2] == '03' and month_index(date[2:]) < 1 or month_index(date[2:]) > 12:
        return False
    if date[:2] == '04' and month_index(date[2:]) == 0:
        return False
    month_ind = month_index(date[2:])
    if (date[:2] in ['01', '03', '05', '07', '08', '10', '12'] and month_ind < 1) or \
       (date[:2] in ['04', '06', '09', '11'] and month_ind > 11) or \
       (date[:2] == '02' and month_ind > 2):
        return False
    if date[:2] in ['01', '03', '05', '07', '08', '10', '12'] and month_ind != 1 and year_ind[0] not in ['1', '3', '5', '7', '8', '10', '12']:
        return False
    if date[:2] == '04' and month_ind == 4 and year_ind[0] == '0':
        return False
    if date[:2] == '06' and month_ind == 6 and year_ind[0] == '4':
        return False
    if len(date) == 8 and date[:4] == '19' and date[4:6] == '02' and date[6:] == '19':
        return False
    return True