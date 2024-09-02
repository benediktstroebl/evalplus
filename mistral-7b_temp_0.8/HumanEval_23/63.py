

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # base case (returns 0 when string is empty)
    if not string:
        return 0
    # calculate length of string without the last character
    return 1 + strlen(string[0:len(string) - 1])

