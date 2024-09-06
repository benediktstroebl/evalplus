

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_characters = set()
    for character in string:
        if character not in unique_characters:
            unique_characters.add(character)

    return len(unique_characters)
