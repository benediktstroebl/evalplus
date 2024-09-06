

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # convert to lower-case
    string = string.lower()
    # get the set of characters
    set_of_chars = set(string)
    # return the size of the set of characters
    return len(set_of_chars)
