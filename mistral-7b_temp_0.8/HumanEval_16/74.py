

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if len(string) == 0:
        return 0
    string = string.lower()
    seen = set()
    for char in string:
        seen.add(char)
    return len(seen)

