

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    count = 0
    for char in string:
        if char.lower() not in distinct_chars:
            distinct_chars.add(char.lower())
            count += 1
    return count