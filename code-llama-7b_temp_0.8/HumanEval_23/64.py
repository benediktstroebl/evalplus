

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    i: int = 0
    while i < len(string):
        i += 1
    return i
