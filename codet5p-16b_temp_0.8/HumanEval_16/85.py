

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_characters_count = 0
    for character in string.lower():
        if string.lower().count(character) == 1:
            distinct_characters_count += 1
    return distinct_characters_count
