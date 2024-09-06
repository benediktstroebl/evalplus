

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
    if s0 == s1:
        return True
    
    if len(s0)!= len(s1):
        return False

    d0 = {}
    d1 = {}
    for c in s0:
        if c not in d0:
            d0[c] = 1
        else:
            d0[c] += 1

    for c in s1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1

    for k, v in d1.items():
        if k not in d0 or d0[k]!= v:
            return False

    return True
    

