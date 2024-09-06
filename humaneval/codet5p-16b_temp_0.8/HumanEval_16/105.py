

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    d = dict()
    for c in string.lower():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return len(d)
