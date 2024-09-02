

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not string:
        return 0

    count = 0
    previous_char = string[0]
    for char in string[1:]:
        if char.lower() == previous_char.lower():
            count += 1
        else:
            count = 1
            previous_char = char
    return count
