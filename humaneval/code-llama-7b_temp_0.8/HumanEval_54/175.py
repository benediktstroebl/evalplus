

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
    # If lengths are different, return False
    if len(s0) != len(s1):
        return False
    # Check each character of the two words
    for i in range(len(s0)):
        # If the characters are not the same, return False
        if s0[i] != s1[i]:
            return False
    # Otherwise, return True
    return True

