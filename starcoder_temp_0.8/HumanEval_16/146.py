

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    count = {}
    for char in string:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return len(count)

