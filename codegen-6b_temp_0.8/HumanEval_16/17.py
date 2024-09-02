

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))

assert count_distinct_characters('xyzXYZ') == 3, 'count_distinct_characters("xyzXYZ")'
assert count_distinct_characters('Jerry') == 4, 'count_distinct_characters("Jerry")'
assert count_distinct_characters('Merry') == 4, 'count_distinct_characters("Merry")'
