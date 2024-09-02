

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    map_count = defaultdict(int)
    for char in string:
        map_count[ord(char)] += 1
    return len(set(map_count.keys()))