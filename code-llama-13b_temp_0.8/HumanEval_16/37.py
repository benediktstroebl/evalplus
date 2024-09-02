

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Check if the input is a string
    if not isinstance(string, str):
        return 0

    # If the input is a string, return the number of distinct characters in it
    return len({x.lower() for x in string})

