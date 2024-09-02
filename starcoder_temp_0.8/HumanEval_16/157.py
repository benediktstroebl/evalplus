

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # for letter in string:
    #     if letter.lower() not in distinct_characters:
    #         distinct_characters.append(letter.lower())
    return len(set(string.lower()))

