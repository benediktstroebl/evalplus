
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
    # my code

    def is_integer(number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def is_valid_month(month):
        try:
            int(month)
            if month < 1 or month > 12:
                return False
            return True
        except ValueError:
            return False

    def is_valid_day(day):
        if int(day) > 31:
            return False
        return True

    def is_valid_date(day, month, year):
        if int(month) == 2:
            if is_integer(day) and is_integer(month) and is_integer(year):
                if int(day) <= 29 and int(month) <= 12 and int(year) >= 1900:
                    return True
            return False
        elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 
