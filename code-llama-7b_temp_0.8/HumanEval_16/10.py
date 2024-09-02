

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # My first solution
    # char_set = set(string.lower())
    # return len(char_set)
    # A more pythonic way to do the same thing
    # We use a set comprehension to convert a string to a set of characters
    # Then we convert the set back to a string, and count the characters
    # Finally we return the length
    return len(set(char.lower() for char in string))

