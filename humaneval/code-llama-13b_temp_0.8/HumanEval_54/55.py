

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
    if s0 == s1:
        return True
    d = {}
    for ch in s0:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for ch in s1:
        if ch in d and d[ch] > 0:
            d[ch] -= 1
        else:
            return False
    return True

