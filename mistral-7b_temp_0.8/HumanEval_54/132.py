

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
    # inverted sets for checking if a string is in the set
    s0_set = set(s0)
    s1_set = set(s1)

    # find the set that's smaller
    s0_len = len(s0_set)
    s1_len = len(s1_set)
    if s0_len > s1_len:
        temp = s0_set
        s0_set = s1_set
        s1_set = temp

    for c in s0_set:
        if c not in s1_set:
            return False
    return True

