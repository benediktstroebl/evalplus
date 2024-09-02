

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # 1. Extract all lower-case chars
    # 2. Use a set to remove duplicates (no case-sensitivity)
    # 3. Return the length of the set
    return len(set(string.lower()))
