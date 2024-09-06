

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

    count0 = {}
    for c in s0:
        if c not in count0:
            count0[c] = 1
        else:
            count0[c] += 1

    for c in s1:
        if c not in count0:
            return False
        count0[c] -= 1

    for c in count0.keys():
        if count0[c] != 0:
            return False

    return True

