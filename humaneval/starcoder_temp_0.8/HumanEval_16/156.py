

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    result = 0
    seen_chars = set()
    for char in string:
        if char.lower() not in seen_chars:
            result += 1
        seen_chars.add(char.lower())
    return result

