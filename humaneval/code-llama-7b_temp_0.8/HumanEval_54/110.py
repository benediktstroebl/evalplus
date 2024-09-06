

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
    for i in s0:
        if i not in d0:
            d0[i] = 1
        else:
            d0[i] += 1
    d1 = {}
    for i in s1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    return d0 == d1

