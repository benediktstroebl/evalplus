

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
    if len(s0) != len(s1):
        return False
    d0 = {}
    for c in s0:
        if c not in d0:
            d0[c] = 1
        else:
            d0[c] += 1
    d1 = {}
    for c in s1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1
    return all(d0[k] == d1[k] for k in d0)

