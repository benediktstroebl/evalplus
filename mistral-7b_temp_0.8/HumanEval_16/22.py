

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = {}
    for char in string:
        char = char.lower()
        if char not in distinct_chars:
            distinct_chars[char] = 1
        else:
            distinct_chars[char] += 1
    return len(distinct_chars)

