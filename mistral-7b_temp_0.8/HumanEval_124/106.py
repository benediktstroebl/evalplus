
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
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    if month.isdigit() and day.isdigit() and year.isdigit():
        if (int(day) >= 1 and int(day) <= 31) and (int(month) >= 1 and int(month) <= 12):
            if (month == "02" and (int(year) % 4 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0)) and int(day) <= 29):
                if int(day) <= 31 and int(month) == 3 or int(day) <= 30 and int(month) == 5 or int(day) <= 31 and int(month) == 8 or int(day) <= 30 and int(month) == 10 or int(day) <= 31 and int(month) == 12:
                    return True
                else:
                    return
