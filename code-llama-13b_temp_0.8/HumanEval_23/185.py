

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string == '':
        return 0
    length = 0
    for i in string:
        length += 1
    return length
