

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
    dict0 = {}
    for item in s0:
        if item not in dict0:
            dict0[item] = 0
        dict0[item] += 1
    for item in s1:
        if item not in dict0:
            return False
        dict0[item] -= 1
        if dict0[item] < 0:
            return False
    return True

