

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    counter = 0
    characters = []
    for letter in string:
        if letter.lower() not in characters:
            characters.append(letter.lower())
            counter += 1
    return counter

