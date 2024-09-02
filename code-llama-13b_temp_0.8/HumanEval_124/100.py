
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

    import datetime

    date = date.strip()

    # 1. The date string is not empty.
    if len(date) == 0:
        return False
    
    # 2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    try:
        if len(date) != 10:
            return False
        day = date[3:5]
        month = date[0:2]
        year = date[6:10]
        # 3. The months should not be less than 1 or higher than 12.
        if int(month) not in range(1, 13):
            return False
        # 4. The date should be in the format: mm-dd-yyyy
        datetime.datetime.strptime(date, "%m-%d-%Y")
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) not in range(1, 32):
                return False
        elif int(month) in [4, 6, 9, 11]:
            if int(day) not in range(1, 31):
                return False
        elif int(month) == 2:
            if int(year) % 4 == 0:
                if int(day) not in range(1, 30):
                    return False
            else:
                if int(day) not in range(1, 29):
                    return False
        return True
    except:
        return False
