
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
    month_to_day = {1: 31,
                    2: 29,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    try:
        months = [int(i) for i in date.split('-')[0]]
        days = [int(i) for i in date.split('-')[1]]
        years = [int(i) for i in date.split('-')[2]]
        if len(days) != len(months) or len(days) != len(years):
            return False

        if len(days) != 1 and len(days) > 30:
            return False

        if len(months) < 1 or len(months) > 12:
            return False

        if len(years) < 1:
            return False

        if days[0] < 1 or days[0] > 31:
            return False

        if months[0] < 1 or months[0] > 12:
            return False

        if months[1] < 1 or months[1] > 12:
            return False

        if months[2] < 1:
            return False

        if days[1] < 1 or days[1] > month_to_day[months[0]]:
            return False

        if days[2] < 1 or days[2] > years[2]:
            return False

        return True
    except ValueError:
        return False

