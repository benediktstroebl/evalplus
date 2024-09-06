

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_chars = set()
    for char in string:
        if char.lower() not in unique_chars:
            unique_chars.add(char.lower())
    return len(unique_chars)

