

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lst = list(string)
    count = 0
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i] = lst[i].lower()

    lst = ''.join(lst)
    return len(set(lst))
