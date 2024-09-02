

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_set = set()
    count = 0
    for c in string:
        if c.upper() not in char_set:
            char_set.add(c.upper())
            count += 1
    return count