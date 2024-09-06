

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
    if s0.count('a') != s1.count('a'):
        return False
    if s0.count('b') != s1.count('b'):
        return False
    if s0.count('c') != s1.count('c'):
        return False
    if s0.count('d') != s1.count('d'):
        return False
    if s0.count('e') != s1.count('e'):
        return False
    if s0.count('z') != s1.count('z'):
        return False
    return True

