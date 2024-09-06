

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    assert string, "Empty string!"
    distinct_characters_in_string = set()
    for character in string:
        distinct_characters_in_string.add(character.lower())
    return len(distinct_characters_in_string)

