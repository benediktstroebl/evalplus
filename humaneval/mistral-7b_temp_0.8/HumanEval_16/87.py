

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    counted_chars = set()
    for char in string.lower():
        if char in counted_chars:
            continue
        counted_chars.add(char)
    return len(counted_chars)

