

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_count = {}
    for char in string:
        if char.lower() not in char_count:
            char_count[char.lower()] = char_count.get(char.upper(), 0) + 1
        else:
            char_count[char.upper()] += 1
    return sum(char_count.values())
