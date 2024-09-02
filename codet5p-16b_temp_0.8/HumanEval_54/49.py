

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

    if len(s0)!= len(s1):
        return False

    def same_chars_helper(s0_ch: str, s1_ch: str):
        if len(s0_ch)!= len(s1_ch):
            return False
        else:
            return all(s0_ch[i] == s1_ch[i] for i in range(len(s0_ch)))

    return all(same_chars_helper(s0_ch, s1_ch) for s0_ch, s1_ch in zip(s0, s1))
