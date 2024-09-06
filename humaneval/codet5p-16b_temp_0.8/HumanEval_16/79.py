

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_count = 0
    string_dict = {}
    for char in string:
        if char not in string_dict:
            string_dict[char] = 0
        string_dict[char] += 1
        distinct_count += 1
    return distinct_count

