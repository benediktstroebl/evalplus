import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())

    # Month range validation
    if (dd < 1 or dd >=[1,3,5,7,8,10,12].map(lambda x: 31 if x in [1,3,7,8,10,12] else 30).get(mm, 31)) and \
       (dd < 1 or dd >=[4,6,9,11].map(lambda x: 30).get(mm, 31)) and dd<1 or dd>29:
        return False

    # Year validation
    if 1>yyyy or yyyy>9999:
        return False

    # Date format validation
    if not re.match(r'(\d\d)-(\d\d)-(\d{4})', date):
        return False

    return True