

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

    c0 = {}
    c1 = {}
    for c in s0:
        if c in c0:
            c0[c] += 1
        else:
            c0[c] = 1
    for c in s1:
        if c in c1:
            c1[c] += 1
        else:
            c1[c] = 1
    return len(c0) == len(c1) and c0 == c1

