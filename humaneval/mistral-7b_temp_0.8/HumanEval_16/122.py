

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Note: this method is quite naive. It iterates over the string twice: once to find all the characters and the
    # second time to count the distinct ones.

    distinct_chars = set()

    for char in string:
        distinct_chars.add(char.lower())

    return len(distinct_chars)

