

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
    d0 = {}
    d1 = {}
    for c0 in s0:
        if c0 in d0:
            d0[c0] += 1
        else:
            d0[c0] = 1
    for c1 in s1:
        if c1 in d1:
            d1[c1] += 1
        else:
            d1[c1] = 1

    return d0 == d1
