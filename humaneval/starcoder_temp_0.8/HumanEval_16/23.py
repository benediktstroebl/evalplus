

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Set
    # set does not allow duplicates, so when you add a duplicate, it won't be added
    # https://docs.python.org/3.7/tutorial/datastructures.html
    # https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset
    return len(set(string))

