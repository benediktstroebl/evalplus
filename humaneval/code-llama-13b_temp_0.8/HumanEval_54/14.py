

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
    s0_dict = {}
    s1_dict = {}
    for i in range(len(s0)):
        if s0[i] not in s0_dict:
            s0_dict[s0[i]] = 0
        s0_dict[s0[i]] += 1
        if s1[i] not in s1_dict:
            s1_dict[s1[i]] = 0
        s1_dict[s1[i]] += 1
    for k in s0_dict:
        if k not in s1_dict or s0_dict[k] != s1_dict[k]:
            return False
    return True

