

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    len = 0
    while True:
        try:
            string[len]
            len += 1
        except IndexError:
            break
    return len

