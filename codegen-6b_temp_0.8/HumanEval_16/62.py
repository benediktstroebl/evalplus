

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # count_of_distinct_characters = len(set(string))
    # return int(count_of_distinct_characters)
    return len(set([c for c in string]))

