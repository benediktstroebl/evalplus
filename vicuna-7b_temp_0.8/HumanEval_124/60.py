
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
    month_dict = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
                  "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
    if date.strip() == "":
        return False
    d = date.split("/")
    if len(d) < 2 or len(d) > 3:
        return False
    for i in range(3):
        if int(d[i]) < 1 or int(d[i]) > 12:
            return False
    mm, dd, yyyy = map(int, d[:2])
    if mm < 1 or mm > 12:
        return False
    if mm == 2 and dd < 1 or dd > 29:
        return False
    if dd > days_allowed(yyyy):
        return False
    return True
