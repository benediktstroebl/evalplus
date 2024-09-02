

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
    char_dict = {}
    for i in range(len(s0)):
        if s0[i] not in char_dict:
            char_dict[s0[i]] = 1
        else:
            char_dict[s0[i]] += 1
    for j in range(len(s1)):
        if s1[j] in char_dict:
            char_dict[s1[j]] -= 1
        else:
            return False
    for k in char_dict.keys():
        if char_dict[k] != 0:
            return False
    return True

