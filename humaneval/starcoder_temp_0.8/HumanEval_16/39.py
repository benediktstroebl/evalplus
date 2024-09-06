

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Make a dict for counting
    counts = {}
    for character in string:
        # Get the character in lower case
        character = character.lower()
        # If it's not seen before, add it in
        if character not in counts:
            counts[character] = 0
        # Increment the count
        counts[character] += 1
    return len(counts)

