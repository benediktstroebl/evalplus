

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    if len(string) < 1:
        return 0

    visited = set()
    for char in string:
        if char in visited:
            continue
        visited.add(char.lower())

    return len(visited)
