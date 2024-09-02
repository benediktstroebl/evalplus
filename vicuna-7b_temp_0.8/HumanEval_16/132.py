

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string_lower = string.lower()
    character_counter = {}
    for char in string_lower:
        if char.isalpha():
            character_counter[char.lower()] = character_counter.get(char.lower(), 0) + 1
    return len(character_counter)
