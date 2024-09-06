

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    set_of_chars = set()
    for char in string:
        set_of_chars.add(char.lower())
    return len(set_of_chars)
