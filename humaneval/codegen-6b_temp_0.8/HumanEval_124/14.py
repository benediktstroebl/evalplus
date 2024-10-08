
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
    valid = False
    try:
        mo, day, yr = map(int, date.split('-'))
        is_valid_month = mo in range(1, 13)
        is_valid_day = day in range(1, 32)
        is_valid_year = yr in range(1, 10000)

        is_valid_day_month = (
            (
                mo in [4, 6, 9, 11] and day in range(1, 30)
            ) or
            (
                mo in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 31)
            ) or
            (
                mo in [2] and day in range(1, 29)
            )
        )

        if (is_valid_month and is_valid_day and is_valid_year and
                is_valid_day_month):
            valid = True

    except:
        pass

    return valid


