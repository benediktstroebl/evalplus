

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # keep a count of the number of characters found in the given string
    count: int = 0

    # iterate over each character in the given string
    for char in string:
        count += 1

    # return count of characters in the given string
    return count

