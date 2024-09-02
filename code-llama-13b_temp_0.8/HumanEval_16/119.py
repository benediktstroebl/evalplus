

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Solution 1. Using set
    # return len({character for character in string})
    # Solution 2. Using dictionary
    # return len({character.lower() for character in string})
    # Solution 3. Using set and dict comprehension
    return len({character.lower() for character in string})

