

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    characters_dict = {}
    for char in string:
        if char.lower() in characters_dict:
            characters_dict[char.lower()] += 1
        else:
            characters_dict[char.lower()] = 1
    return len(characters_dict.keys())

