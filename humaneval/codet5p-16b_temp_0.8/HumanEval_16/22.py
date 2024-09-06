

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    string = string.lower()
    unique_chars = set()
    for ch in string:
        if ch.isalpha():
            unique_chars.add(ch)
    return len(unique_chars)
