import re
def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    """
    # Define validation rules
    DATE_PATTERN = re.compile(r'^[0-9]{2}-[0-9]{2}-[0-9]{4}$')
    DAY_RULES = {1: [1, 31], 2: [1, 29], 3: [1, 31], 4: [1, 30],
                5: [1, 31], 6: [1, 30], 7: [1, 31], 8: [1, 31],
                9: [1, 30], 10: [1, 31], 11: [1, 30], 12: [1, 31]}
    MONTH_RULES = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}
    
    # Check if date string matches the date pattern and apply day and month rules
    if DATE_PATTERN.match(date) and validates_day(date, DAY_RULES, MONTH_RULES) and validates_month(date, MONTH_RULES):
        return True
    else:
        return False
def validates_day(date, DAY_RULES, MONTH_RULES):
    day, month, _ = map(int, date.split('-'))
    if 1 <= month <= 12:
        return 1 <= day <= DAY_RULES[month]
    else:
        return False
def validates_month(date, MONTH_RULES):
    return 1 <= MONTH_RULES[int(date.split('-')[1])] <= 12