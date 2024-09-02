
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
    if len(date) < 1:
        return False
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    split = date.split('-')
    date_YYYY = split[2]
    date_MM = split[0]
    date_DD = split[1]
    if len(date_YYYY) != 4 or int(date_YYYY) < 1 or int(date_YYYY) > 9999:
        return False
    if len(date_MM) == 1 and date_MM in months:
        if len(date_DD) == 1 and date_DD in days:
            return True
    if len(date_MM) == 2 and date_MM in months:
        if len(date_DD) == 2 and date_DD in days:
            return True
    if len(date_MM) == 2 and date_MM not in months:
        return False
    if len(date_MM) == 3 and date_MM in months:
        if len(date_DD) == 2 and date_DD in days:
            return True
    if len(date_MM) == 3 and date_MM not in months and int(date_MM) != 12:
        return False
    if len(date_MM) == 3 and date_MM in months and int(date_MM) == 12:
        if len(date_DD) == 2 and date_DD in days:
            return True
    if len(date_MM) == 3 and date_MM not in months and int(date_MM) != 12:
        return False
    if len(date_MM) > 3 and int(date_MM) != 12:
        return False
    if len(date_DD) > 2:
        return False
    return False
