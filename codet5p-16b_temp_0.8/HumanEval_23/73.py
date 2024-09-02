

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    if not isinstance(string, str):
        raise TypeError("Parameter should be a string")

    return len(string)
