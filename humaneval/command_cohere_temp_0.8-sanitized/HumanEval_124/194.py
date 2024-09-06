import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.strip()
        date = date.split('-')
        mm, dd, yyyy = map(int, date)

        if 1 <= mm <= 12:
            first_rule = 1 <= dd <= days_in_month[mm]
        else:
            first_rule = False

        second_rule = 1 <= mm <= 12
        third_rule = 2000 <= yyyy <= 3000
        fourth_rule = re.match(r"^[0-9]{2}-[0-9]{2}-[0-9]{4}$", date[0:3] + '-' + date[3:])

        return first_rule and second_rule and third_rule and fourth_rule
    except:
        return False
days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}