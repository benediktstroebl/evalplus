

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    new_string = []
    for c in string.lower():
        if c not in new_string:
            new_string.append(c)
    return len(new_string)

