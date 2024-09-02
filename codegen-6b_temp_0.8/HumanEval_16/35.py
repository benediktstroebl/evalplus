

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # This involves figuring out the size of the set of characters in the string. We can do this by mapping
    # the character to an index.
    char_to_index = {}
    for i, char in enumerate(string):
        if char not in char_to_index:
            char_to_index[char] = i
    return len(char_to_index)

