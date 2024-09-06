

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
    d = {}
    for c0, c1 in zip(s0, s1):
        if c0 not in d or c1 not in d:
            d[c0] = 1
            d[c1] = 1
        else:
            d[c0] += 1
            d[c1] += 1
    return not any(d[c] for c in s0)
