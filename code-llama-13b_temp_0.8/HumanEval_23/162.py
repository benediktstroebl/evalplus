

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    cnt = 0
    for i in string:
        cnt += 1
    return cnt

