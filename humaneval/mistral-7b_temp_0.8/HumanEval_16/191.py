

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.upper()
    output = 0

    for i in string:
        if string.count(i) > 1:
            continue
        output += 1

    return output
