

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    strings = set()
    for char in string.lower():
        # Remember the case
        if char in strings:
            strings.remove(char)
        else:
            strings.add(char)
    return len(strings)
