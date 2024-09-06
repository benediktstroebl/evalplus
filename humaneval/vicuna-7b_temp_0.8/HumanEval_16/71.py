

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    seen = set()
    n = len(string)
    result = 0
    for i in range(n):
        char = string[i]
        if char in seen:
            result += 1
            seen.add(char)
        else:
            seen.add(char)
            result += 1
    return result
