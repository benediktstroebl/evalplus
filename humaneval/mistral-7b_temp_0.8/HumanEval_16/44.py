

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # initialize a set
    distinct_chars = set()
    # iterate through each char
    for char in string:
        # add the char to the set, ignoring case
        distinct_chars.add(char.lower())
    # return the length of the set
    return len(distinct_chars)
