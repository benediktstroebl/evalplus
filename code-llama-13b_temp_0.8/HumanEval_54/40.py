

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
    d0 = dict()
    d1 = dict()
    for c0 in s0:
        d0[c0] = d0.get(c0, 0) + 1
    for c1 in s1:
        d1[c1] = d1.get(c1, 0) + 1
    if d0.keys() != d1.keys():
        return False
    for k in d0.keys():
        if d0[k] != d1[k]:
            return False
    return True

