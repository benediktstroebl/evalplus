

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    result = 0
    while string[result] != '\0':
        result += 1
    return result

