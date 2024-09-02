

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lower_string = string.lower()
    d = {}
    for char in lower_string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    count = 0
    for value in d.values():
        if value == 1:
            count += 1
    return count

