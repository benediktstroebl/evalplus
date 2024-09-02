

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    count = 0
    while string:
        count += 1
        string = string[1:]

    return count
