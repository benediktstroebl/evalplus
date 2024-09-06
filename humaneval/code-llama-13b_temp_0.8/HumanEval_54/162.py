

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
    dict0 = {}
    dict1 = {}
    for c in s0:
        if c in dict0:
            dict0[c] += 1
        else:
            dict0[c] = 1
    for c in s1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    for c in dict0:
        if c not in dict1 or dict1[c] != dict0[c]:
            return False
    return True

