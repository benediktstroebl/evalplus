

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    length: int = 0
    for letter in string:
        length += 1
    return length
