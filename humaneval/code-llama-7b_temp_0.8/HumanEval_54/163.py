

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
    char_counts0 = {}
    for c in s0:
        if c not in char_counts0:
            char_counts0[c] = 0
        char_counts0[c] += 1

    for c in s1:
        if c not in char_counts0:
            return False
        char_counts0[c] -= 1

    for count in char_counts0.values():
        if count != 0:
            return False
    return True

