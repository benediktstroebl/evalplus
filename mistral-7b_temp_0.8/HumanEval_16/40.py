

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # To prevent having to do a string comparison, we can convert the string to a set
    # and then count the length of that set
    string_set = set(string)

    return len(string_set)

