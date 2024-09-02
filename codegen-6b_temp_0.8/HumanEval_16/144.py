

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # store all lowercase letters in a new list
    characters = []
    for s in string.lower():
        if s not in characters:
            characters.append(s)
    return len(characters)

