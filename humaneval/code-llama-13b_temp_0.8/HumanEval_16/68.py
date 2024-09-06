

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Solution 1 - collections.Counter
    # return len(Counter(string.lower()).keys())

    # Solution 2 - set
    return len({char for char in string.lower()})

