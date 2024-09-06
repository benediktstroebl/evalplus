import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())
    
    # Month checks
    if (dd<1) or (dd>=[1,3,5,7,8,10,12].map(lambda x: x+1).get(mm, 31)):
        return False
    if mm==2 and dd>29:
        return False
    if mm==4 or mm==6 or mm==9 or mm==11 and dd>30:
        return False

    # Year checks
    if mm<1 or mm>12:
        return False
    if yyyy<2000 or yyyy>2030:
        return False

    return True