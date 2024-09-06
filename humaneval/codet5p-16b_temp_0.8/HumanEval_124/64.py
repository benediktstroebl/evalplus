
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

    if date!= '':
        months = ['1', '3', '5', '7', '8', '10', '12']
        days = [1, 31, 30, 29]
        days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        date_split = date.split('-')
        date_day = int(date_split[0])
        date_month = int(date_split[1])
        date_year = int(date_split[2])

        if date_month < 1 or date_month > 12:
            return False
        if date_day < 1 or date_day > days_in_month[date_month]:
            return False
        if date_month in months and date_day > days[months.index(date_month)]:
            return False
        if date_month in months and date_day > days_in_month[date_month]:
            return False
