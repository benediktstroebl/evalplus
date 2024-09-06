

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.upper()
    characters = []
    for character in string:
        if character in characters:
            continue
        characters.append(character)
    return len(characters)
