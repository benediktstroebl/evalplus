

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    new_list = []
    for char in string:
        if char.isupper():
            new_list.append(char.lower())
        else:
            new_list.append(char)
    return len(set(new_list))
