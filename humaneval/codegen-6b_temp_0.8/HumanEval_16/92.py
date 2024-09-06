

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    count = 1
    for c in string:
        if string.index(c) != 0:
            if c.lower() == c:
                count += 1
            else:
                count -= 1
    return count
