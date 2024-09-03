def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>>strlen(' With more text.')
    13
    """
    return len(string)