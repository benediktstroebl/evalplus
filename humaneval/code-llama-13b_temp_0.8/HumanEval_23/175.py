

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string == '':
        return 0
    count = 0
    for char in string:
        count += 1
    return count

