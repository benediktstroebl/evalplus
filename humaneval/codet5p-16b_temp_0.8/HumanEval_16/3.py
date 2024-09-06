

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    count = 0
    string_lower = string.lower()
    for c in string_lower:
        if c in string_lower:
            count += 1
    return count
