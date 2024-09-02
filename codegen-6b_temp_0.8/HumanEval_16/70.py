

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lower = set(string.lower())
    res = len(lower)
    if res == 1:
        return res

    # for upper in lower:
    #     if upper != upper.upper():
    #         res -= 1
    # return res

    return res

