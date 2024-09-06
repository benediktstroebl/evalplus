

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    set_chars = set()
    for ch in string:
        if ch.lower() not in set_chars:
            set_chars.add(ch)

    return len(set_chars)
