

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
    s0_dict = {}
    s1_dict = {}

    for c in s0:
        s0_dict[c] = s0_dict.get(c, 0) + 1

    for c in s1:
        s1_dict[c] = s1_dict.get(c, 0) + 1

    return s0_dict == s1_dict

