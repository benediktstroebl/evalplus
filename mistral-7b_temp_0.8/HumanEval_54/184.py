

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
    # to store the characters of each string
    s0_chars = set(s0)
    s1_chars = set(s1)
    # print(s0_chars, s1_chars)
    # return s0_chars == s1_chars
    return s0_chars.issubset(s1_chars) and s1_chars.issubset(s0_chars)

