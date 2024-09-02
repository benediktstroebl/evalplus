

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = {}
    count = 0
    for char in string:
        if char.lower() not in distinct_characters:
            count += 1
            distinct_characters[char.lower()] = count
    return count