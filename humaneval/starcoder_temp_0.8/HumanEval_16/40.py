

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    count = {}
    for ch in string:
        count[ch.lower()] = count.get(ch.lower(), 0) + 1

    return len(count)
