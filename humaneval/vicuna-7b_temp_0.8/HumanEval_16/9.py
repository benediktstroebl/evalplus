

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    character_set = frozenset()
    for char in string:
        if char in character_set:
            character_set.discard(char)
        else:
            character_set.add(char)
    return len(character_set)