
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
    if date.strip() == '':
        return False
    
    month_days = {}
    months = [1,3,5,7,8,10,12]
    days_limit = [31,30,31,30,31,30,31]
    months_limit = set(range(1,13)) - set(months)
    
    for i in range(len(date)):
        month = int(date[i:i+2]) - 1
        if month not in months_limit:
            return False
        if 31 != days_limit[months[month]-1] and date[i+2] not in str(days_limit[months[month]-1]):
            return False
        month_days[month] = days_limit[months[month]-1]
    
    day = int(date[-1:])
    if day < 1 or day > 31:
        return False
    if 30 != day and day not in str(day):
        return False
    return True
