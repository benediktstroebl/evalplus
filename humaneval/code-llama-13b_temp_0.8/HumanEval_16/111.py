

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # if string == '':
    #     return 0
    #
    # l_string = string.lower()
    #
    # unique_chars = set()
    # for char in l_string:
    #     if char not in unique_chars:
    #         unique_chars.add(char)
    #
    # return len(unique_chars)

    if string == '':
        return 0

    return len(set(string.lower()))

