

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Initialize the counter
    characters = {}
    # Iterate through the string
    for char in string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    # Count and return the number of distinct characters
    return len(characters)

