

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Solution 1
    return len(set(string.lower()))

    # Solution 2
    # if len(string) == 0:
    #     return 0
    # chars = set()
    # for char in string:
    #     if char.lower() not in chars:
    #         chars.add(char.lower())
    # return len(chars)
