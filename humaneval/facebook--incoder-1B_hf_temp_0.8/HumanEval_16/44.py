def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_count = 0
    for char in string:
        if char.isupper():
            char_count += 1
        elif char.islower():
            char_count -= 1
    return char_count

