
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

    months = ["01", "03", "05", "07", "08", "10", "12"]
    leap_months = ["01", "03", "05", "07", "08", "10", "12"]
    months = months + months + leap_months

    if not date:
        return False
    elif date[-5:] == "02-29" and date[-8:-6] not in leap_months:
        return False
    elif date[-5:] == "02-29" and date[-8:-6] in leap_months and int(date[-4:]) % 4 != 0:
        return False
    elif date[-5] == "02" and date[-8:-6] not in leap_months:
        return False
    elif int(date[-5:-3]) > 12 or int(date[-5:-3]) < 1:
        return False
    elif int(date[-8:-6]) in months and int(date[-5:-3]) != 2 and int(date[-8:-6]) > 12 or int(date[-8:-6]) in months and int(date[-5:-3]) != 2 and int(date[-8:-6]) < 1:
        return False
    elif int(date[-8:-6]) in leap_months and int(date[-5:-3]) == 2 and int(date[-4:]) % 4 != 0:
        return False
    elif int(date[-8:-6]) in months and int(date[-5:-3]) == 2 and int(date[-8:-6]) > 12 or int(date[-8:-6]) in months and int(date[-5:-3]) == 2 and int(date[-8:-6]) < 1:
        return False
    elif int(date[-5:-3]) == 2 and int(date[-8:-6]) not in leap_months and int(date[-4:]) > 29 or int(date[-5:-3]) == 2 and int(date[-8:-6]) not in leap_months and int
