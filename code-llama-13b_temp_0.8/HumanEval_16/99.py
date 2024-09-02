

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    seen = set()
    for char in string:
        if char.lower() not in seen:
            seen.add(char.lower())
    return len(seen)

