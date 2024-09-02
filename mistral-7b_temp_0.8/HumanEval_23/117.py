

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Count the characters
    counter = 0
    while string[counter] != '\0':
        counter += 1

    return counter

