

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if len(string) == 0:
        return 0
    else:
        return strlen(string[1:]) + 1


