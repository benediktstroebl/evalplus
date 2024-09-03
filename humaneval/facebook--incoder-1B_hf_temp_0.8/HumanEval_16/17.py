def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if len(string) == 0:
        return 0

    chars = {character: 0 for character in string}

    for character in string:
        if character in chars:
            chars[character] += 1

    return len(chars)

