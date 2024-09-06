

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    ind = 0;
    for c in string:
        ind += 1
    return ind
