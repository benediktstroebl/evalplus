

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    map = {}
    for c in string:
        if c.lower() not in map:
            map[c.lower()] = 1
        else:
            map[c.lower()] += 1
    return len(map)