
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
    months = {"01":31, "03":31, "05":31, "07":31, "08":31, "10":31, "12":31}
    months_30 = {"04":30, "06":30, "09":30, "11":30}

    if len(date) == 0:
        return False

    try:
        month, day, year = date.split("-")
        if month not in months and month not in months_30:
            return False
        elif month == "02":
            if int(day) > 29:
                return False
            elif int(year) % 4 == 0 and int(day) > 28:
                return False
        elif month in months_30 and int(day) > 30:
            return False
        else:
            if int(day) > int(months[month]):
                return False
    except:
        return False

    return True

