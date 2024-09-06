

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    unique_characters: int = 0

    for character in string:
        if character.lower() in unique_characters:
            continue
        else:
            unique_characters += 1
    return unique_characters
