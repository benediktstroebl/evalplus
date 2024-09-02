

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # traverse the string keeping track of characters we have already seen
    # return the length of the set at the end

    char_set = set()

    for char in string:
        char_set.add(char.lower())

    return len(char_set)

    # this could be made faster by checking if the lower case version of the current character is in our set, and if it
    # is, we don't add it again.
    # this approach would be slower in the case that the input string is mostly upper case, but faster if it has equal
    # amounts of lower case and upper case letters.
