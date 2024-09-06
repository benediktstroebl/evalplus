

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    result = 0
    lowered_string = string.lower()
    for letter in lowered_string:
        if letter not in lowered_string[0:result]:
            result += 1
    return result

