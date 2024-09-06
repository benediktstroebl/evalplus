

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = str(string).lower() # convert to lowercase for case-insensitive comparison
    count = {}
    for char in string:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return len(count)