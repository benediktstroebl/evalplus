

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    seen_set = set()

    for char in string:
        lower_char = char.lower()

        if lower_char not in seen_set:
            seen_set.add(lower_char)

    return len(seen_set)

