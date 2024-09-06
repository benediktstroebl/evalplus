

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    characters = {}

    for c in string:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return len(characters.keys())

