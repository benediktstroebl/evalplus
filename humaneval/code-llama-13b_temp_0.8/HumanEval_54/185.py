

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    # sets are used to store the characters of the strings
    # a set is used to store the first string's characters
    chars0 = set()

    # a set is used to store the second string's characters
    chars1 = set()

    # loop through the strings and add the characters to the sets
    for i in range(0, len(s0)):
        chars0.add(s0[i])

    for i in range(0, len(s1)):
        chars1.add(s1[i])

    # the two strings have the same characters if their
    # sets have the same number of items
    return len(chars0) == len(chars1)

