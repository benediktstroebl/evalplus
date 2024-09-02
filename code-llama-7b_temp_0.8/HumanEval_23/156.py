

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    len_result = 0
    for _ in string:
        len_result += 1
    return len_result
