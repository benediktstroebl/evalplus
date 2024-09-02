

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    mapping = {c.lower(): i for i, c in enumerate(string)}
    return sum(1 for c in string.lower() if c in mapping)