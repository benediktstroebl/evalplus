

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not isinstance(string, str):
        raise TypeError('Argument must be of type str')
    return len(string)

