

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    store = {}
    for char in string:
        if char in store:
            store[char] += 1
        else:
            store[char] = 1
    return len(store)
