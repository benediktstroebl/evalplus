
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
    if not date:
        return False
    day, month, year = date.split("-")
    if len(day) == 1 and len(month) == 1 and len(year) == 4:
        if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
            if day.isdigit() and (1 <= int(day) <= 31):
                if (1 <= int(month) <= 12):
                    if (1 <= int(day) <= 30):
                        if (int(year) % 400 == 0) or (int(year) % 4 == 0) and (int(year) % 100!= 0):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return
