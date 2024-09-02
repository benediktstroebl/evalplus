
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
    # replace this for solution
    import datetime

    def time_difference(first_date, second_date):
        return abs((first_date - second_date).days)

    months = {
        1: 31,
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
        12: 31
    }

    def invalid_date(date):
        parts = date.split("-")
        if len(parts) != 3:
            return True
        if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
            return True
        try:
            day_int = int(parts[1])
            month_int = int(parts[0])
            year_int = int(parts[2])
        except:
            return True
        if day_int > months.get(month_int) or month_int > 12 \
                or day_int < 1 or year_int < 1:
            return True
        else:
            return False

    def check_date(date, check_strings):
        parts = date.split("-")
        if len(parts) != 3:
            return False
        if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
            return False
        try:
            day_int = int(parts[1])
            month_int = int(parts[0])
            year_int = int(parts[2])
        except:
            return False
        if day_int > months.get(month_int) or month_int > 12 \
                or day_int < 1 or year_int < 1:
            return False
        if not all(x in check_strings for x in parts[0:3]):
            return False
        return True

    def check_date_str(date):
        if not date.strip():
            return False
        if len(date.split("-")) != 3:
