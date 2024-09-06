

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
    assert type(s0) == str, 'Input must be a string'
    assert type(s1) == str, 'Input must be a string'
    if len(s0) != len(s1):
        return False
    else:
        for i in range(len(s0)):
            if s0[i] != s1[i]:
                return False
        return True

