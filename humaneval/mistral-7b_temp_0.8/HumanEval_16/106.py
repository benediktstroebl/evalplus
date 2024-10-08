

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if string is None:
        return None

    set_of_characters = set()

    for char in string:
        if char.isalnum():
            set_of_characters.add(char)

    return len(set_of_characters)
