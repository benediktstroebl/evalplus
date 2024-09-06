

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    characters = []
    for character in string:
        if character.islower():
            characters.append(character)
        else:
            characters.append(character.upper())
    return len(set(characters))
