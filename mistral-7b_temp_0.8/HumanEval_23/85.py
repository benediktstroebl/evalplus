

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    string_length = 0
    for i in string:
        string_length += 1
    return string_length
