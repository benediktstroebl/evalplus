

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
    # for each character in s0, if it's in the same position in s1,
    # and is different from the other characters in s0, then return False
    for i in range(len(s0)):
        if s0[i] != s1[i] and s0[i] not in s1[0:i] and s0[i] not in s1[i+1:]:
            return False
    return True
