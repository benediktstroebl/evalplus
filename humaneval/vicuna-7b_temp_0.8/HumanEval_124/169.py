
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
    if not date or not date.strip():
        return False
    if len(date) < 1 or len(date) > 31:
        return False
    if (date[:2] != '06' and date[:2] != '07' and date[:2] != '08' and date[:2] != '09' and
        date[:2] != '10' and date[:2] != '11' and date[:2] != '12' and
        date[:2] != '04' and date[:2] != '06' and date[:2] != '05' and
        date[:2] != '12' and date[:2] != '13'):
        return False
    if (date[:1] < '1' or date[:1] > '12' or date[date.index('-')+1] < '1' or
        date[date.index('-')+1] > '31'):
        return False
    month = date[:date.index('-')].isalpha()
    day = date[date.index('-')+1:].isdigit()
    year = date[date.index('-')+3:].isdigit()
    return (month == True and day >= 1 and day <= 31 and year >= 40 and year <= 99)
