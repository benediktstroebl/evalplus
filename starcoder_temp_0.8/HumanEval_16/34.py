

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")
    # Use set to remove duplicates
    return len(set(string))
