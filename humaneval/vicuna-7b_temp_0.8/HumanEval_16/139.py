

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    n = len(string)
    count = 0
    for i in range(n):
        if string[i] in string[i+1:]:
            count += 1
        else:
            count += 1
    return count