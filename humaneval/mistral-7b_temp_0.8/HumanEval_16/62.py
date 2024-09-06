

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_count = 0
    char_set = set()
    for char in string:
        char_set.add(char.upper())
    for char in string:
        if char.lower() in char_set:
            unique_count += 1
    return unique_count

