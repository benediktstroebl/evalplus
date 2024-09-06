

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not string:
        return 0
    if len(string) == 1:
        return 1
    first_char = string[0]
    second_char = string[1]
    return 1 + count_distinct_characters(string[2:]) + \
        count_distinct_characters(string[1:])
