

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    counter = {}
    for char in string:
        char = char.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return len(counter)

