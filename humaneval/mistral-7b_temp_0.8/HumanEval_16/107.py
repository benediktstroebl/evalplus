

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    if not string:
        return 0

    # Use a set to remove duplicates and then convert back to a list
    # 1.
    string_set = set(string)
    string_set = list(string_set)

    # 2.
    # string_set.sort()

    return len(string_set)

