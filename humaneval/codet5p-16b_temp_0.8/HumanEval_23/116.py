

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    len_str = 0
    for i in string:
        len_str += 1
    return len_str
