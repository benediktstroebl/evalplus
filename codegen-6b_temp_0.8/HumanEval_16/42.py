

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = str.lower(string)
    characters = {}
    for character in string:
        characters[character] = characters.get(character, 0) + 1
    return len(characters.keys())

assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
