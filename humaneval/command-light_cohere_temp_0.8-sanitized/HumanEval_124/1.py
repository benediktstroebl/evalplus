import re
def valid_date(date):
    """
    Validate date string according to the format mm-dd-yyyy
    """
    # use regex to validate the date format
    date_regex = re.compile('^\Date: \d{1}[/-]\d{3}-[/-]\d{4}')
    return date_regex.isMatch(date)