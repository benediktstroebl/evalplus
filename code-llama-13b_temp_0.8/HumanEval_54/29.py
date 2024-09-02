

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
    s0_set = set(s0)
    s1_set = set(s1)
    if len(s0_set) != len(s1_set):
        return False

    s0_dict = {}
    for c in s0:
        if c in s0_dict:
            s0_dict[c] += 1
        else:
            s0_dict[c] = 1

    for c in s1:
        if c not in s0_dict:
            return False
        else:
            s0_dict[c] -= 1
            if s0_dict[c] == 0:
                del s0_dict[c]

    if len(s0_dict) == 0:
        return True
    else:
        return False

