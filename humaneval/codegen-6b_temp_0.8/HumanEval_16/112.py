

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = [c for c in set(string.lower()) if c.isalpha() and c.islower()]
    return len(distinct_characters)
test_count_distinct_characters()

