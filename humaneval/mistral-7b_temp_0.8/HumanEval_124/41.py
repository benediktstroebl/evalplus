
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

    date_split = date.split('-')

    if date_split[0] == '0' and date_split[1] == '0':
        return False
    else:
        date_split_1 = date_split[1].split('-')
        date_split_2 = date_split[2].split('-')

        # get month and day number
        month_number = int(date_split[0])
        day_number = int(date_split[1])
        year_number = int(date_split[2])

        if 0 < month_number <= 12 and 0 < day_number <= 31 and 0 < year_number <= 3000:

            # get the number of days in the given month
            number_of_days = 31

            if month_number == 1:
                number_of_days = 28
            elif month_number == 3:
                number_of_days = 31
            elif month_number == 5:
                number_of
