
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
    date_valid = False
    if len(date) != 0:
        date_valid = True

    if date_valid:
        date_format = date.split('-')

        try:
            month = date_format[0]
            day = date_format[1]
            year = date_format[2]
        except:
            return False

        if (month.isnumeric() and day.isnumeric() and year.isnumeric()):
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 0 and month < 13:
                if day > 0:
                    if month in (1,3,5,7,8,10,12):
                        if day < 32:
                            date_valid = True
                        else:
                            date_valid = False
                    if month in (4,6,9,11):
                        if day < 31:
                            date_valid = True
                        else:
                            date_valid = False
                    if month == 2:
                        if day < 30:
                            date_valid = True
                        elif day == 29:
                            if year % 4 == 0 and year % 100 != 0:
                                date_valid = True
                            elif year % 400 == 0:
                                date_valid = True
                            else:
                                date_valid = False
                        else:
                            date_valid = False
                else:
                    date_valid = False
            else:
                date_valid = False
        else:
            date_valid = False

    return date_valid

