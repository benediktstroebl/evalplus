
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
    month = int(date[:3])
    day = int(date[3:])
    year = int(date[5:])

    if day > 31 or day < 1 or (month == 2 and day > 29) or (month >= 13 and month <= 2) or (month < 1 or month > 12):
        return False

    if year < 1000 or year >= 9999:
        return False

    if month == 4 and day == 6 and year % 400 == 0 or (month == 6 and day == 6 and year % 4 == 0):
        if day < 1 or day > 30:
            return False
    return True

for i in range(1, 11):
    date = valid_input("Enter a valid date in the format mm-dd-yyyy: ")
    if not valid_date(date):
        print("Invalid date: ", date)
    else:
        print("Valid date: ", date)
    print("---------------------------------------------------------------------")
