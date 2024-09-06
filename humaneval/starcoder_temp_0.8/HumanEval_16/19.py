

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # make the string lowercase
    string = string.lower()
    # initialise a dictionary to count the characters
    character_counts = {}
    for character in string:
        if character not in character_counts:
            # each character must appear at least once
            character_counts[character] = 1
        else:
            # increment the counter by 1
            character_counts[character] += 1
    return len(character_counts.keys())
