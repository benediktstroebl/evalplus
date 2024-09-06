
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
    assert isinstance(date, str), 'The date should be a string'
    assert date!= '', 'The date should not be empty'
    if len(date.split('-'))!= 3:
        return False
    month, day, year = date.split('-')
    assert int(month) in range(1,13), 'The month must be in range 1 to 12'
    assert int(day) in range(1,32), 'The day must be in range 1 to 31'
    assert int(year) in range(2000, 2050), 'The year should be in the 2000 to 2050'
    if len(date.split('-')) == 3:
        assert int(day) in range(1,31) or int(day) in range(1,30) and int(month) in [4,6,9,11], 'The date should be in the format mm-dd-
