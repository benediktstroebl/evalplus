

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    #TODO: Implement the function
    counter = 0
    for char in string:
        counter += 1
    return counter

