

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # iterative
    count = 0
    for char in string:
        count += 1

    return count

    # recursive
    if string == '':
        return 0
    return 1 + strlen(string[1:])

