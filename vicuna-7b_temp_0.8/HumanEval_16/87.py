

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    mapping = {ord(char): i for i, char in enumerate(string)}
    count = 0
    for char in string:
        count += mapping[ord(char)]
    return count