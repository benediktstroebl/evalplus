
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
    m = re.match(r'(\d{2})-(\d{2})-(\d{4})', date)
    if m:
        (d1, d2, d3) = m.groups()
        if (d1 == '01' or d1 == '03' or d1 == '05' or d1 == '07' or d1 == '08' or d1 == '10' or d1 == '12') and (d2 == '31') and (d3 == '2000') :
            return True
        if (d1 == '04' or d1 == '06' or d1 == '09' or d1 == '11') and (d2 == '30') and (d3 == '2020'):
            return True
        if (d1 == '02') and (d2 == '29'):
            return True
        if (d1 == '02') and (d2 == '28'):
            return True
    return False
    pass
