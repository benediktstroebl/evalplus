

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

    for index in range(len(s0)):
        if s0[index] not in s0_dict:
            s0_dict[s0[index]] = 1
        else:
            s0_dict[s0[index]] += 1

        if s1[index] not in s1_dict:
            s1_dict[s1[index]] = 1
        else:
            s1_dict[s1[index]] += 1

    if sum(s0_dict.values()) != sum(s1_dict.values()):
        return False

    return True
