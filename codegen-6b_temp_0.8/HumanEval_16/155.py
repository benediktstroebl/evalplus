

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Another way of doing this is by converting to lower case and doing the count
    # string = string.lower()
    # return len(set(string))

    # Another way is to create a set of distinct characters from the string and then adding
    # the length of the string
    string_set = set(string)
    return len(string_set)
