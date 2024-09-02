

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    counter = 0
    for character in string:
        counter += 1
    return counter
