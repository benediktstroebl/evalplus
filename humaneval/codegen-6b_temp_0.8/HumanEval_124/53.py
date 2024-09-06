
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
    reg_day = r'^[01][0-9][0-9][0-9]' # 0-9
    reg_month = r'^[01][0-9][0-9]' # 00-99
    reg_year = r'^[0-9][0-9][0-9]' # 0-99
    reg_day_len = r'([0-9]{1,2}|30|31)'

    day = re.findall(reg_day, date)
    month = re.findall(reg_month, date)
    year = re.findall(reg_year, date)

    if len(day) > 0 and len(month) > 0 and len(year) > 0:
        if (
                int(month[0]) > 0 and int(month[0]) <= 12 and
                int(day[0]) > 0 and int(day[0]) <= 31):
            return True
        elif (
                int(month[0]) == 4 or int(month[0]) == 6 or int(month[0]) == 9 or int(month[0]) == 11
                and int(day[0]) > 0 and int(day[0]) <= 30):
            return True
        elif (
                int(month[0]) == 2 and int(day[0]) > 0 and int(day[0]) <= 29):
            return True
        else:
            return False
    else:
        return False


