

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

    s0 = s0.replace(" ", "")
    s1 = s1.replace(" ", "")

    s0_dict = {}
    for c in s0:
        if c in s0_dict:
            s0_dict[c] += 1
        else:
            s0_dict[c] = 1

    s1_dict = {}
    for c in s1:
        if c in s1_dict:
            s1_dict[c] += 1
        else:
            s1_dict[c] = 1

    for key in s0_dict.keys():
        if key not in s1_dict:
            return False
        if s0_dict[key] != s1_dict[key]:
            return False

    return True

