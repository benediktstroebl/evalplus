

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    lower_chars = []
    for char in string.lower():
        lower_chars.append(char)

    lower_chars = set(lower_chars)
    return len(lower_chars)

