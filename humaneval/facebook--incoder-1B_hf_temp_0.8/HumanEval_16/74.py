def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if string is None:
        return 0
    hashval = hash(string)
    count = 0
    for char in string:
        if hashval & char!= 0:
            count += 1
        hashval >>= 1
    return count

