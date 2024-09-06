
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
    from datetime import datetime
    month_map = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    day_pattern = re.compile(r'[0-9]{2}')
    month_pattern = re.compile(r'[0-9]{2}')
    year_pattern = re.compile(r'[0-9]{4}')
    if date == '':
        return False
    else:
        day = day_pattern.findall(date)
        month = month_pattern.findall(date)
        year = year_pattern.findall(date)
        if day[0] < 1 or day[0] > 31:
            return False
        if month[0] < 1 or month[0] > 12:
            return False
        if month[0] in ['02']:
            if len(year[0]) != 4:
                return False
            if year[0][:2] < '19' or year[0][:2] > '20':
                return False
            if int(year[0][:2])%4==0 and int(year[0][2:])%4==0:
                if year[0][2:] > '29':
                    return False
                elif int(year[0][:2])%4!=0 and year[0][2:] > '28':
                    return False
            else:
                return False
        if month[0] in ['04','06','09','11']:
            if int(day[0]) < 1 or int(day[0]) > 30:
                return False
        if month[0] in ['01','03','5,7,8,10,12']:
            if int(day[0]) < 1 or int(day[0]) > 31:
                return False
        if
