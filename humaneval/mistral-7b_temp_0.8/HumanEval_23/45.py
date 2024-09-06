

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    string_len = 0
    for i in string:
        string_len += 1
    return string_len

