

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
    i0 = 0
    i1 = 0
    m = len(s0)
    n = len(s1)
    while i0 < m and i1 < n:
        if s0[i0] != s1[i1]:
            i0 = i0 + 1
        i1 = i1 + 1
    if i0 == m:
        return i1 == n
    else:
        return False
