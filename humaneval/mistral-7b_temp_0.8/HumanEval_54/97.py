

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

    ls0 = list(s0)
    ls1 = list(s1)

    d = {}

    for c in ls0:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in ls1:
        if c not in d or d[c] == 0:
            return False
        d[c] -= 1

    return True

