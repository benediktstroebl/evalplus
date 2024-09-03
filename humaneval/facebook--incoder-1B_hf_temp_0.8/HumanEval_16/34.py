def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_count = {}
    i = 0
    for ch in string:
        if ch not in char_count:
            char_count[ch] = 1
            i += 1
        else:
            char_count[ch] += 1
    return i

