

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    mapping = {}
    count = 0
    for char in string:
        if char.lower() not in mapping:
            mapping[char.lower()] = 1
            count += 1
    return count
