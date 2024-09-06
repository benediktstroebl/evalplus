
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
    months = ['01', '03', '05', '07', '08', '10', '12']
    if len(date.strip()) == 0:
        return False
    if date[-4:] == '-2021':
        return True
    if date[-4:] == '-2022':
        return True
    if date[-4:] == '-2023':
        return True
    if date[-4:] == '-2024':
        return True
    if date[-4:] == '-2025':
        return True
    if date[-4:] == '-2026':
        return True
    if date[-4:] == '-2027':
        return True
    if date[-4:] == '-2028':
        return True
    if date[-4:] == '-2029':
        return True
    if date[-4:] == '-2030':
        return True
    if date[-4:] == '-2031':
        return
