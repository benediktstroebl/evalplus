

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    histogram = {}
    for char in string:
        histogram[char.lower()] = histogram.get(char.lower(), 0) + 1
    return len(histogram)
