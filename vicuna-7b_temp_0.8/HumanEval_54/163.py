

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
    # check the length of the words
    if len(s0) != len(s1):
        return False

    # check if the words are empty
    if not s0 and not s1:
        return True

    # check if the words are not empty and have the same length
    if len(s0) == len(s1) and s0 == s1:
        return True

    # check if the words are not empty and have different lengths
    if len(s0) != len(s1):
        return False

    # check if the words are not empty and have different characters
    if set(s0) != set(s1):
        return False

    # check if the words are empty or have the same characters
    return True
