

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    string = string.lower()
    chars = dict()
    for c in string:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return len(chars)

