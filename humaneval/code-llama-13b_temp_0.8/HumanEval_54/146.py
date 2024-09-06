

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
    s0_counter = {}
    s1_counter = {}
    for c in s0:
        if c in s0_counter:
            s0_counter[c] += 1
        else:
            s0_counter[c] = 1
    for c in s1:
        if c in s1_counter:
            s1_counter[c] += 1
        else:
            s1_counter[c] = 1
    for c in s0_counter:
        if c not in s1_counter or s1_counter[c] < s0_counter[c]:
            return False
    return True

