

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    distinct_characters = 0
    for character in string:
        if not character.isalpha():
            continue
        character = character.lower()
        if character not in distinct_characters:
            distinct_characters += 1
    return distinct_characters

