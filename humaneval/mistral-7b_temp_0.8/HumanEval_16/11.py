

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Add your code here
    if len(string) == 0:
        return 0
    # string = string.lower()
    temp_set = set()
    for x in string:
        temp_set.add(x)
    return len(temp_set)

