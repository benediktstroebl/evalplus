
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
    # This is a failing test, so make it pass!

    # Split date by '-' and assign to a list
    date_list = date.split('-')

    # Convert each element of the list to a integer
    date_list = [int(i) for i in date_list]

    # Check that the length of the list is 3
    if len(date_list)!= 3:
        return False

    # Check that the first element is between 1 and 12
    if date_list[0] < 1 or date_list[0] > 12:
        return False

    # Check that the second element is between 1 and 31, according to the month
    if date_list[1] < 1 or date_list[1] > 31:
        if date_list[0] in [1, 3, 5, 7, 8, 10, 12]:
            return False
        elif date_list[0] in [4, 6, 9, 11]:
            return False
        elif date_list[0] == 2:
            if date_list[1] > 29:
                return False
    # Check that the third element is between 1900 and 2099
    if date_list[2] < 1900 or date_list[2] > 2099:
        return False

    # Otherwise, return True
    return True
