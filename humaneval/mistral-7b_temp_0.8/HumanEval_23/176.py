

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string == '':
        return 0
    elif string[0] == '\n':
        return 1
    return 1 + strlen(string[1:])

