

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # make sure that the input string is in lower-case
    lower_case_string = string.lower()

    # create a dictionary with key as the character and value as the count of that character in the string
    character_count_map: dict[str, int] = {}
    for character in lower_case_string:
        if character not in character_count_map:
            character_count_map[character] = 0
        character_count_map[character] += 1

    # now count the number of keys in the dictionary
    return len(character_count_map)
