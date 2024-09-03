def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    letters_to_count = {}
    for c in string:
        letters_to_count[c.lower()] = letters_to_count.get(c.lower(), 0) + 1
    return len(letters_to_count)

