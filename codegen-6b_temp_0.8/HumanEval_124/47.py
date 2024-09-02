
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
    # Your code here
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', \
              'Oct', 'Nov', 'Dec']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    valid_date = validate_date(date)
    split_date = valid_date.split('-')
    month = split_date[0]
    day = split_date[1]
    year = split_date[2]

    if month.isdigit() and year.isdigit() and day.isdigit():
        month = int(month)
        day = int(day)
        year = int(year)
            
        if month > 0 and month <= 12:
            if day > 0 and day <= days[month-1]:
                if year > 0 and year <= 9999:
                    return True
    return False
