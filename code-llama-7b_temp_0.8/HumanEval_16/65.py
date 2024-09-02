

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # return len(set(string))  # Using the set
    # Using the dictionary
    counts = {}
    for character in string:
        if character.lower() in counts:
            continue
        counts[character.lower()] = True
    return len(counts)

