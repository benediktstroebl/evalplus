

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    char_set = set()

    for c in string.lower():
        if c in char_set:
            continue
        else:
            char_set.add(c)

    return len(char_set)

