

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    char_counts = {}
    for char in string:
        char_lower = char.lower()
        if char_lower not in char_counts:
            char_counts[char_lower] = 1
        else:
            char_counts[char_lower] += 1
    return len(char_counts.keys())

