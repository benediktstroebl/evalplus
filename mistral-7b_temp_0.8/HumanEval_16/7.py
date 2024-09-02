

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lowercase_string = string.lower()

    chars_set = set()
    for char in lowercase_string:
        if char not in chars_set:
            chars_set.add(char)

    return len(chars_set)

