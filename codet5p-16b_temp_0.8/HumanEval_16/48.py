

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    count_distinct = 0
    for char in string:
        if char.lower() not in string.lower():
            count_distinct += 1
    return count_distinct

