def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Note: this assumes that the input is lowercase. Would be nice to handle upper and lowercase here
    # but it is easier just to test the upper/lowercase distinctions
    return len(set(string).difference(string.lower()))

