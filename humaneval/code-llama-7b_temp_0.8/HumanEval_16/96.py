

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # your code goes here
    new_string = string.lower()
    new_list = []
    for char in new_string:
        if char not in new_list:
            new_list.append(char)

    return len(new_list)
