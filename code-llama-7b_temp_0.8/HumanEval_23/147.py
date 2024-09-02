

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # BAD
    # index = 0
    # for char in string:
    #     index += 1
    # return index

    # GOOD
    return len(string)

