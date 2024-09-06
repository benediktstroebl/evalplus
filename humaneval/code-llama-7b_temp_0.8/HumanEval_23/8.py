

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    size = 0
    for i in range(len(string)):
        if string[i] != '':
            size = size + 1
    return size

