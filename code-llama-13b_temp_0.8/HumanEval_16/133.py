

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    lowered_string = string.lower()
    result = {}
    for char in lowered_string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return len(result)
