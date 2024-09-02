

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Solution 1
    # return len({char.lower() for char in string})

    # Solution 2
    # return len(set(string.lower()))

    # Solution 3
    # return len({ord(char.lower()) for char in string})

    # Solution 4
    # return len({chr(ord(char) | 32) for char in string})

    # Solution 5
    # return len(set(string.lower()) | set(string.upper()))

    # Solution 6
    return len({ord(char.lower()) for char in string})

