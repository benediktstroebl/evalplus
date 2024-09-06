

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
    d = dict()
    for ch in s0:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    for ch in s1:
        if ch not in d:
            return False
        else:
            d[ch] -= 1
            if d[ch] < 0:
                return False
    return True


