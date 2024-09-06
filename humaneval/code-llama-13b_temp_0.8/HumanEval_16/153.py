

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Assuming lowercase letters (a-z) and uppercase letters (A-Z) have different codes.
    # In ASCII, lowercase letters (97-122) and uppercase letters (65-90) have consecutive codes.
    # Therefore, by subtracting lowercase letters from uppercase letters,
    # we get the code difference of the letters.
    # Example:
    # For 'J', the ord() function returns 74,
    # for 'e', the ord() function returns 101,
    # for 'r', the ord() function returns 114,
    # for 'r', the ord() function returns 114,
    # for 'y', the ord() function returns 121
    # So the result of 74 - 101 + 114 + 114 + 121 = 155

    return sum([ord(c) - 96 for c in string.lower()])

