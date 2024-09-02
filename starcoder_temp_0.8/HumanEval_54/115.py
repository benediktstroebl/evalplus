

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
    #
    # s0 = 'eabcdzzzz'
    # s1 = 'dddzzzzzzzddeddabc'
    # s0 = 'abcd'
    # s1 = 'dddddddabc'
    # s0 = 'dddddddabc'
    # s1 = 'abcd'
    # s0 = 'eabcd'
    # s1 = 'dddddddabc'
    # s0 = 'abcd'
    # s1 = 'dddddddabce'
    # s0 = 'eabcdzzzz'
    # s1 = 'dddzzzzzzzddddabc'
    #
    chars_s0 = sorted(s0)
    chars_s1 = sorted(s1)
    for i in range(len(chars_s0)):
        if chars_s0[i]!= chars_s1[i]:
            return False
    return True
