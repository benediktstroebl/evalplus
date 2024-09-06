

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    result = 0
    for i in range(0, len(string)):
        result += 1
    return result

