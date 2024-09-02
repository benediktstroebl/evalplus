

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

    s0_count = {}
    s1_count = {}

    for c in s0:
        if c in s0_count:
            s0_count[c] += 1
        else:
            s0_count[c] = 1

    for c in s1:
        if c in s1_count:
            s1_count[c] += 1
        else:
            s1_count[c] = 1

    return s0_count == s1_count
