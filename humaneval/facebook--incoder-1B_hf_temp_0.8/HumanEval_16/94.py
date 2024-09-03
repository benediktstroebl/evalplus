def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    chars = set()
    for char in string:
        chars.update(char for ch in string.lower() if ch in string.ascii_letters)
    chars.update(c for c in string.ascii_letters if c in chars)
    return len(chars)

