

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
    if not s0:
        return True
    if len(s0) != len(s1):
        return False
    d0 = {c: s0.count(c) for c in set(s0)}
    d1 = {c: s1.count(c) for c in set(s1)}
    for c in d0.keys():
        if c not in d1:
            return False
        if d0[c] != d1[c]:
            return False
    return True

