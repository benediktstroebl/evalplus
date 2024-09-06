
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
    days_of_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    try:
        date = date.split('-')
        m = date[0]
        d = date[1]
        y = date[2]
        assert len(date) == 3
        assert m.isdigit()
        assert d.isdigit()
        assert y.isdigit()
        if int(m) <= 0 or int(m) > 12:
            return False
        if int(d) <= 0 or int(d) > days_of_months[int(m)]:
            return False
        if int(y) <= 0:
            return False
    except AssertionError:
        return False
    return
