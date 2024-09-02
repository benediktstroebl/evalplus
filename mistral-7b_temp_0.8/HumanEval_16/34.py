

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()
    uniq_characters = set()
    for char in string:
        uniq_characters.add(char)
    return len(uniq_characters)
