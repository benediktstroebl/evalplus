

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
    s0_d = {}
    for ch in s0:
        if ch in s0_d:
            s0_d[ch] += 1
        else:
            s0_d[ch] = 1
    s1_d = {}
    for ch in s1:
        if ch in s1_d:
            s1_d[ch] += 1
        else:
            s1_d[ch] = 1
    return s0_d == s1_d

