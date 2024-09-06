

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

    for i in s0:
        if i in s0_dict:
            s0_dict[i] += 1
        else:
            s0_dict[i] = 1

    for i in s1:
        if i in s1_dict:
            s1_dict[i] += 1
        else:
            s1_dict[i] = 1

    return s0_dict == s1_dict

