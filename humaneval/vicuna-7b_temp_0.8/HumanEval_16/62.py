

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.upper()
    distinct_chars = {}
    for char in string:
        if char.isalpha():
            if char.upper() in distinct_chars:
                distinct_chars[char.upper()] += 1
            else:
                distinct_chars[char.upper()] = 1
    return len(distinct_chars)
