

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Temporary count
    distinct_characters = 0

    # Keep track of characters already seen
    char_seen = []

    # Loop through the string
    for char in string:
        if char not in char_seen:
            char_seen.append(char)
            distinct_characters += 1

    return distinct_characters

