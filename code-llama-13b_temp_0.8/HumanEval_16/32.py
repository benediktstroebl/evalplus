

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    seen_chars = set()
    for char in string:
        char_lower = char.lower()
        seen_chars.add(char_lower)
    return len(seen_chars)
