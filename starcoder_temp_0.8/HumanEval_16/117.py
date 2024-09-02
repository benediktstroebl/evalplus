

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_set = set()
    for letter in string:
        unique_set.add(letter.lower())
    return len(unique_set)

