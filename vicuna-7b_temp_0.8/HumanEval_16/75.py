

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # create a set of all characters in the string, regardless of case
    characters = set(string.lower())

    # count the number of elements in the set
    return len(characters)