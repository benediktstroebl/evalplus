
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
    def parse(date):
        valid_date = []

        if len(date) != 10:
            return False

        valid_date.append(int(date[0]) == 0 or int(date[0]) == 1 or int(date[0]) == 2)
        valid_date.append(int(date[1]) == 0 or int(date[1]) == 1 or int(date[1]) == 2)
        valid_date.append(int(date[2]) == 0 or int(date[2]) == 1 or int(date[2]) == 2)
        valid_date.append(int(date[3]) == 0 or int(date[3]) == 1)
        valid_date.append(int(date[4]) == 0 or int(date[4]) == 1 or int(date[4]) == 2)
        valid_date.append(int(date[5]) == 0 or int(date[5]) == 1 or int(date[5]) == 2)
        valid_date.append(int(date[6]) == 0 or int(date[6]) == 1 or int(date[6]) == 2)
        valid_date.append(int(date[7]) == 0 or int(date[7]) == 1 or int(date[7]) == 2)
        valid_date.append(int(date[8]) == 0 or int(date[8]) == 1)
        valid_date.append(int(date[9]) == 0 or int(date[9]) == 1 or int(date[9]) == 2)
        valid_date.append(int(date[1]) > 0 and int(date[1]) < 13)
        valid_date.append(int(date[3]) > 0 and int(date[3]) < 13)
        valid_date.append(int(date[5]) > 0 and int(date[5]) < 13)
        valid_date.append(int(date[7]) > 0 and int(date[7]) < 13)
        valid_date.append(int(date[8]) > 0 and int(date[8]) < 13)
        valid_date.append(int(date[9]) > 0 and int(date[9])