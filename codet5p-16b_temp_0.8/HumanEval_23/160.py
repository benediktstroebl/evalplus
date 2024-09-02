

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    len_of_string = 0
    for element in string:
        len_of_string += 1
    return len_of_string

