

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    char_dict = {}
    for i in string.lower():
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return len(char_dict)

