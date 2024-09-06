

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # This method uses a set to store the distinct characters,
    # which means a set is only able to store unique values.
    distinct_chars = set(string)

    return len(distinct_chars)

