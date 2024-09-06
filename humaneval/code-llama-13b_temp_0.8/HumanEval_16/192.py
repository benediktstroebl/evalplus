

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # solution using sets
    return len(set(string.lower()))

    # solution using iteration
    # distinct_characters = set()
    # for character in string:
    #     distinct_characters.add(character.lower())
    # return len(distinct_characters)

