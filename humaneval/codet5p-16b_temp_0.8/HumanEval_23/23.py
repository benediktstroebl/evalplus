

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    len_ = 0
    for c in string:
        len_ += 1
    return len_

