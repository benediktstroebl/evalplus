

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    current_char = string[0]
    for char in string[1:]:
        if char != current_char:
            distinct_chars.add(current_char)
            current_char = char
    return len(distinct_chars)