

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # set comprehension to remove duplicates
    # return len({char for char in string.lower()})

    # using set, which is more efficient
    return len(set(string.lower()))

