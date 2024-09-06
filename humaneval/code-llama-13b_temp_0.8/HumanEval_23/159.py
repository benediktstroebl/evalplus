

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Leverage recursion to implement tail recursion
    if string == '':
        return 0
    return 1 + strlen(string[1:])

