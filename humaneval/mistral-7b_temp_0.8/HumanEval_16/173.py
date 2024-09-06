

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # we can use a set to keep track of the characters. If the character is unique we will add it to the set.
    # if the character is not unique we will skip it

    # we need to make sure to keep case in mind and account for it
    # we need to make sure to account for non-ascii characters and perhaps convert them to ascii first

    # solution:
    set_of_chars = set()
    for char in string.lower():
        if char.isalpha() and char not in set_of_chars:
            set_of_chars.add(char)

    return len(set_of_chars)

