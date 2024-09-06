
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
    # in order to be valid, a date string must
    # 1. not be empty
    # 2. contain 2 integer separated by dash
    # 3. the first integer should be between 1 and 12
    # 4. the second integer should be between 1 and 31
    # 5. the first integer represents a month
    # 6. the second integer represents a day
    # 7. the last integer represents a year
    # 8. the last integer should be >= 1900 and <= 2099

    # 1. if the date string is empty, return false
    if not date:
        return False

    # 2. split the string into a list of 3 integers
    month, day, year = date.split("-")

    # 3. if any of the integers is not an integer, return false
    if month.isdigit() == False or day.isdigit() == False or year.isdigit() == False:
        return False

    # 4. convert the integers to integers
