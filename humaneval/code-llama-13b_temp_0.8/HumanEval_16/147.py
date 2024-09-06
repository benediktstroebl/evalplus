

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # return len({i for i in string.lower()})

    # return len({string.lower().replace(i, "") for i in string.lower()})

    # return len({i for i in string.lower()})

    # return len(set(string.lower()))

    # return len(set(string.lower()))

    return len(set(string.lower()))

