

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Create a list of all unique characters of the string
    unique_chars = list(set(string))

    # Convert the list to a set, then count the length of the set to find the number of distinct characters
    return len(set(unique_chars))

