

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    my_dict = {}
    for char in string.lower():
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    return len(my_dict)

