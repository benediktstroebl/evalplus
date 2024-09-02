

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert string to list of lowercase characters
    string = string.lower()
    char_count = [0] * 26
    for i in range(len(string)):
        char_count[ord(string[i]) - 97] += 1
    return max(char_count)
