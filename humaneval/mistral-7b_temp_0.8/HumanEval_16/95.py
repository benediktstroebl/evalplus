

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    count_char = 0
    s = string.lower()
    for i in s:
        if s.count(i) == 1:
            count_char += 1
    return count_char

