

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    counter = {}
    for letter in string:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return len(counter)

