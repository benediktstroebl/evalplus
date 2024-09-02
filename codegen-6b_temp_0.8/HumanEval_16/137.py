

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    for character in string:
        if character.lower() not in distinct_chars:
            distinct_chars.add(character.lower())
        elif character.upper() not in distinct_chars:
            distinct_chars.add(character.upper())
    return len(distinct_chars)

