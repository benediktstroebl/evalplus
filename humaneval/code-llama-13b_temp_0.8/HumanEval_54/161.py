

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
    dict_s0 = {}
    dict_s1 = {}

    for char in s0:
        if char in dict_s0:
            dict_s0[char] += 1
        else:
            dict_s0[char] = 1

    for char in s1:
        if char in dict_s1:
            dict_s1[char] += 1
        else:
            dict_s1[char] = 1

    for char in dict_s0:
        if char not in dict_s1:
            return False
        if dict_s0[char] != dict_s1[char]:
            return False

    return True

