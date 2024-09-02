

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_count = {}
    for letter in string.lower():
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return len(char_count)

