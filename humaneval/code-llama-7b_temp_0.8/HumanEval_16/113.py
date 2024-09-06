

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = set()
    for c in string:
        if c.isalpha():
            if c.lower() in distinct_characters:
                continue
            else:
                distinct_characters.add(c.lower())
    return len(distinct_characters)

