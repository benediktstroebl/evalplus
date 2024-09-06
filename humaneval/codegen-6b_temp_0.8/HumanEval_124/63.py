
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
    # I think the logic should be:
    # >>> try:
    # >>>     date_time = datetime.strptime(date, "%m-%d-%Y")
    # >>> except ValueError:
    # >>>     return False
    # >>> else:
    # >>>     days = (date_time.month, date_time.day, date_time.year)
    # >>>     if days in [
    # >>>         (2, 29, 2020),
    # >>>         (2, 28, 2020),
    # >>>         (4, 29, 2020),
    # >>>         (4, 28, 2020),
    # >>>     ]:
    # >>>         return True
    # >>>     if days in [
    # >>>         (1, 31, 2000),
    # >>>         (3, 31, 2000),
    # >>>         (5, 31, 2000),
    # >>>         (7, 31, 2000),
    # >>>         (8, 31, 2000),
    # >>>         (10, 31, 2000),
    # >>>         (12, 31, 2000),
    # >>>     ]:
    # >>>         return True
    # >>>     if days in [
    # >>>         (1, 30, 2016),
    # >>>         (3, 30, 2016),
    # >>>         (5, 30, 2016),
    # >>>         (7, 30, 2016),
    # >>>         (8, 30, 2016),
    # >>>         (10, 30, 2016),
    # >>>         (12, 30, 2016),
    # >>>     ]:
    # >>>         return True
    # >>>     return False

    try:
        datetime.strptime(date, "%m-%d-%Y")
    except:
        return False
    else:
        days = (int(date[5:7]), int(date[8:10]), int(date[0:4]))
        if days in [
            (2, 29, 2020),
            (2, 28, 2020),
            (4, 29, 2020),
            (4, 28, 2020),
        ]:
            return True
        if days in [
            (1, 31, 2016),
            (3