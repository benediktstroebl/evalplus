

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Strategy: use a set to store characters in order to avoid duplicates
    #          the number of distinct characters is the length of the set
    distinct_characters = set()
    for c in string:
        if c.lower() not in distinct_characters:
            distinct_characters.add(c.lower())
    return len(distinct_characters)

