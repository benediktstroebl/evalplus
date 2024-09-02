

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    letter_count = {}
    for char in string.lower():
        letter_count[char] = letter_count.get(char, 0) + 1
    return len(letter_count.keys())

