
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
    try:
        date = datetime.strptime(date, "%m-%d-%Y")
        days = datetime.date.today() - date
        if days.days < 1 or days.days > 31 or (days.days == 31 and date.month != 3 and date.month != 5 and date.month != 7 and date.month != 8 and date.month != 10 and date.month != 12):
            return False
        elif days.days < 1 or days.days > 30 or (days.days == 30 and date.month != 2):
            return False
        elif date.month < 1 or date.month > 12:
            return False
        else:
            return True
    except ValueError:
        return False