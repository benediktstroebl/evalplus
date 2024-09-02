

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    n = len(string)
    distinct_chars = {}
    for i in range(n):
        ch = string[i].lower()
        if ch not in distinct_chars:
            distinct_chars[ch] = 1
        else:
            distinct_chars[ch] += 1
    return len(distinct_chars)