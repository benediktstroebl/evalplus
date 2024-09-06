
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
    def _get_month_index(month):
        return (month + 1) % 12
    def _get_day_index(month, day):
        return (day - 1) % 31 + _get_month_index(month)
    def _get_date_index(year, month, day):
        return (day - 1) % 30 + (month - 1) * 31 + year - 1900
    def _is_valid(year, month, day):
        if year < 1900 or year > 2038 or (month < 1 or month > 12) or (day < 1 or day > 31):
            return False
        if month == 2:
            if day < 1 or day > 29:
                return False
        return True
    def _is_leap(year):
        return (year % 4 == 0 and (year % 100 != 0 or not year % 400))
    year, month, day = map(_get_date_index, date.split('-'))
    if _is_valid(year, month, day) and _is_leap(year):
        return True
    return False
