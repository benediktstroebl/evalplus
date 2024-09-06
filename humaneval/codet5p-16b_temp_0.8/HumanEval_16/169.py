

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    if not isinstance(string, str):
        raise ValueError('argument must be a string')
    string = string.lower()
    return len({char for char in string})

