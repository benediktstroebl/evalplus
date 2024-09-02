

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Use a dictionary to count the distinct characters and check if they are already in the dictionary
    char_count = {}
    for char in string:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return len(char_count)