def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # count all the distinct characters
    letters_count = {}
    for c in string:
        if c not in letters_count:
            letters_count[c] = 0
        letters_count[c] += 1
    # now count the characters in the dict
    return len(letters_count.keys())

