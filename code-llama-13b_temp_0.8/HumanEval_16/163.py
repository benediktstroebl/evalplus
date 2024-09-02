

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Hint 1: Try making a dictionary which will have the character as a key and the number of times it occurs as a value
    # Hint 2: Once you have that, just find out the length of the dictionary and return it
    # Hint 3: The str.lower() method may be useful (i.e., str.lower('XYZ') returns 'xyz')

    distinct_characters = {}

    for character in string:
        character = character.lower()

        if character in distinct_characters:
            continue
        else:
            distinct_characters[character] = 1

    return len(distinct_characters)

