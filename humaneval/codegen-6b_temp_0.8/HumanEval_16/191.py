

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = set()

    for character in string:
        if character.isupper():
            character = character.lower()
        distinct_characters.add(character)
    return len(distinct_characters)
