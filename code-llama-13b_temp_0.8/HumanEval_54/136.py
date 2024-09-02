

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
    d1 = dict()
    for c in s0:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1
    d2 = dict()
    for c in s1:
        if c not in d2:
            d2[c] = 1
        else:
            d2[c] += 1

    for key, value in d1.items():
        if key not in d2:
            return False
        if d2[key] != value:
            return False
    return True

