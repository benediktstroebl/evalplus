
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
    # your code here
    import re
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    invalid = False
    try:
        m = re.search('(\d{1,2})-(\d{1,2})-(\d{4})', date)
        mm, dd, yyyy = m.groups()
        if mm in months and dd in days:
            return True
        elif mm in months and dd not in days:
            invalid = True
        elif mm not in months and dd in days:
            invalid = True
        elif mm not in months and dd not in days:
            invalid = True
    except:
        return False
    if invalid:
        return False
    else:
        return True

    return True
