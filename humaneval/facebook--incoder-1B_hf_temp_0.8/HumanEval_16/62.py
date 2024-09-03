def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # https://stackoverflow.com/questions/33158098/counting-distinct-characters-in-a-string
    return len(set(string.lower()))

