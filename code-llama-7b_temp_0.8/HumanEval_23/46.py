

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # return len(string)
    # Please don't use len
    return sum(1 for _ in string)

