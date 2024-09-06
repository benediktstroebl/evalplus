

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = {}
    previous_char = ''
    for char in string:
        if char.lower() in distinct_characters.values():
            distinct_characters[char.lower()] += 1
        else:
            distinct_characters[char.lower()] = 1
        previous_char = char
    return len(distinct_characters)