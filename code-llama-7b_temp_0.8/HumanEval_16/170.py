

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    characters_counter = 0
    lowercase_string = string.lower()
    for character in lowercase_string:
        if character.isalpha():
            characters_counter += 1
    return characters_counter

