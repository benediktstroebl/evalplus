

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    assert isinstance(string, str)
    if len(string) == 0:
        return 0
    return 1 + strlen(string[1:])

