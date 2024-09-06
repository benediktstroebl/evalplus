

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
    if len(s0) != len(s1): return False

    char_dict = {}
    for i in range(len(s0)):
        if s0[i] not in char_dict:
            char_dict[s0[i]] = [s1[i]]
        else:
            char_dict[s0[i]].append(s1[i])

    for char in s0:
        if char not in char_dict or len(char_dict[char]) > 1:
            return False

    return True

