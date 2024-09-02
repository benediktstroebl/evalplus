

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    #
    #
    #
    lower_case = string.lower()
    distinct = 0
    for i in lower_case:
        if i not in lower_case[lower_case.index(i) + 1:]:
            distinct += 1
    return distinct

