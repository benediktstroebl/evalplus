

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    unique_chars = set()
    for char in string.lower():
        if char.isalpha():
            unique_chars.add(char)
    return len(unique_chars)

