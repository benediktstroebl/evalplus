

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    length = 0
    for i in range(len(string)):
        length = length + 1
    return length

