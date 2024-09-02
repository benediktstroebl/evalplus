

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

    count_s0 = {}
    for c in s0:
        if c in count_s0:
            count_s0[c] += 1
        else:
            count_s0[c] = 1

    count_s1 = {}
    for c in s1:
        if c in count_s1:
            count_s1[c] += 1
        else:
            count_s1[c] = 1

    for c in count_s0:
        if c not in count_s1:
            return False
        if count_s0[c] != count_s1[c]:
            return False

    return True

