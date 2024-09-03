def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # return len(set([ord(c) for c in string]))
    return sum(ord(c) not in string.upper() and (ord(c) not in string.lower()) for c in string)

