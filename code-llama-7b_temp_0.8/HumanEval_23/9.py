

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    if isinstance(string, str):
        return len(string)

    raise TypeError(f'input must be str, not {type(string)}')

