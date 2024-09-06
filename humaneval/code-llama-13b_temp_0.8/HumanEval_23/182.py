

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string:
        return 1 + strlen(string[1:])
    else:
        return 0

