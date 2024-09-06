

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if string == "":
        return 0

    string_lower = string.lower()
    counter = 0

    for char in string_lower:
        if char not in string_lower[counter+1:]:
            counter += 1
    return counter

