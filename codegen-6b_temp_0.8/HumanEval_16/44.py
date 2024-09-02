

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Create a set of chars one at a time
    # Now use the string as a key and increment the list of keys
    # If we encounter a duplicate, we increment a counter
    chars = set()
    for char in string:
        if char in chars:
            chars.add(char)
        else:
            chars.add(char.lower())
        print(chars)
    return len(chars)

