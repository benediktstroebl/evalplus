

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not string:
        return 0
    map_chars = {}
    for char in string:
        if char.lower() in map_chars:
            map_chars[char.lower()] += 1
        else:
            map_chars[char.lower()] = 1
    return len(map_chars)
