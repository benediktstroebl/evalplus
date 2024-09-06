

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = 0
    character_set = set()

    for char in string:
        if char.lower() not in character_set:
            character_set.add(char.lower())
            distinct_characters += 1

    return distinct_characters

