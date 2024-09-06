

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # initialize a counter for each character in the string
    character_counts = {}
    for c in string:
        if c.upper() not in character_counts:
            character_counts[c.upper()] = 1
        else:
            character_counts[c.upper()] += 1

    # add 1 to the count of all characters that are not in the counts dictionary
    for c in string:
        if c.upper() not in character_counts:
            character_counts[c.upper()] = 1

    return sum(character_counts.values())
