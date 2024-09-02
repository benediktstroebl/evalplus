

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    lenght = 0
    for i in string:
        lenght += 1
    return lenght
