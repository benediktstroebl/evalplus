
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
    try:
        days = {
            '01': 31,
            '02': 28,
            '03': 31,
            '04': 30,
            '05': 31,
            '06': 30,
            '07': 31,
            '08': 31,
            '09': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }

        months = {
            '01': 31,
            '02': 28,
            '03': 31,
            '04': 30,
            '05': 31,
            '06': 30,
            '07': 31,
            '08': 31,
            '09': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }

        parsed_date = date.split('-')

        return (
            len(parsed_date) == 3 and
            (len(parsed_date[1]) == 2 and 1 <= int(parsed_date[1]) <= 12 and
             0 < int(parsed_date[2]) <= years[parsed_date[0]]) or
            (len(parsed_date[1]) == 1 and 1 <= int(parsed_date[0]) <= 12 and
             0 < int(parsed_date[1]) <= months[parsed_date[0]] and
             0 < int(parsed_date[2]) <= years[parsed_date[0]]) or
            (len(parsed_date[0]) == 2 and 1 <= int(parsed_date[0]) <= 12 and
             0 < int(parsed_date[1]) <= days[parsed_date[0]] and
             0 < int(parsed_date[2]) <= years[parsed_date[0]]) or
            (len(parsed_date[0]) == 1 and 0 <= int(parsed_date[0]) <= 12 and
             0 < int(parsed_date[1]) <= days[parsed_date[0]] and
             0 < int(parsed_date[2