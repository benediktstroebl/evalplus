

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
    # s0_freq = {}
    # for c in s0:
    #     if c not in s0_freq:
    #         s0_freq[c] = 1
    #     else:
    #         s0_freq[c] += 1
    # s1_freq = {}
    # for c in s1:
    #     if c not in s1_freq:
    #         s1_freq[c] = 1
    #     else:
    #         s1_freq[c] += 1
    # return s0_freq == s1_freq
    return set(s0) == set(s1)

