

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    result = 0
    count = 0
    for char in string:
        count = 0
        for c in string:
            if char == c:
                count += 1
        if count == 1:
            result += 1
    return result

