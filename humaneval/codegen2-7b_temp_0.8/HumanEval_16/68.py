

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    result = 0
    for i in range(len(string)):
        result += 1 if string[i]!= string[i].lower() else 0
    return result

