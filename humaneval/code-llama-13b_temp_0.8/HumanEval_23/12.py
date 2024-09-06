

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not string:
        return 0
    count = 0
    for i in string:
        count += 1
    return count

