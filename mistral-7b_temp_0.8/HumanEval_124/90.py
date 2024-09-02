
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
    # Write your code here
    # You can check the date type by using the type function
    if type(date) == str:
        return False
    if date.isalpha():
        return False
    date = date.split("-")
    if len(date) != 3:
        return False
    try:
        a = int(date[0])
        b = int(date[1])
        c = int(date[2])
    except:
        return False
    if a < 1 or a > 12:
        return False
    if b < 1 or b > 31:
        return False
    if b > 31 and a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        return False
    if b > 30 and a == 2:
        return False
    if b > 30 and a == 4 or a == 6 or a == 9 or a == 11:
        return False
    if c < 
