

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # strlen = 0
    # for c in string:
    #     strlen += 1
    # return strlen

    # strlen = 0
    # for _ in string:
    #     strlen += 1
    # return strlen

    strlen = 0
    for char in string:
        strlen += 1
    return strlen

