

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # Empty string
    if string == '':
        return 0

    # Iterate over chars
    length = 0
    for char in string:
        length += 1
    return length

