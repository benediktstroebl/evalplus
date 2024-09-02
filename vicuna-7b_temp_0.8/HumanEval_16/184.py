

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_count = {}
    current = string[0]
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[current] += 1
        current = char
    return len(char_count)