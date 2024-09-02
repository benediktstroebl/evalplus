

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct = 0
    visited = set()
    for char in string:
        if char.lower() not in visited:
            distinct += 1
            visited.add(char.lower())
    return distinct

