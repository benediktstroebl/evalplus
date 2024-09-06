

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

    c0 = dict()
    c1 = dict()
    for c in s0:
        c0[c] = c0.get(c, 0) + 1
    for c in s1:
        c1[c] = c1.get(c, 0) + 1

    if len(c0)!= len(c1):
        return False

    for c in c0.keys():
        if c0[c]!= c1[c]:
            return False

    return True
