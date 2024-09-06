

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_chars = set()
    for char in string:
        lower_case_char = char.lower()
        if lower_case_char not in unique_chars:
            unique_chars.add(lower_case_char)
    return len(unique_chars)

