

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
    s0_dict = dict()
    for s in s0:
        if s0_dict.get(s) is None:
            s0_dict[s] = 1
        else:
            s0_dict[s] += 1

    s1_dict = dict()
    for s in s1:
        if s1_dict.get(s) is None:
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1

    if len(s0_dict) != len(s1_dict):
        return False
    for key in s0_dict:
        if s0_dict[key] != s1_dict[key]:
            return False
    return True

