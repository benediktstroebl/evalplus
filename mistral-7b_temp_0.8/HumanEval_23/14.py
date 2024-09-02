

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # return len(string)
    length = 0
    while string:
        length += 1
        string = string[1:]
    return length

