

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

    # sorting both strings
    s0 = sorted(s0)
    s1 = sorted(s1)

    # checking if the length of the two strings is the same
    if len(s0) != len(s1):
        return False

    # iterating over the first string
    for i in range(len(s0)):
        # if the characters are not the same
        if s0[i] != s1[i]:
            return False

    # if it passes the tests, then the characters are the same
    return True

