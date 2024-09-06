

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

    assert len(s0) == len(s1)
    chars = {}
    for c in s0:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c in s1:
        if c not in chars or chars[c] == 0:
            return False
        chars[c] -= 1
    return True

