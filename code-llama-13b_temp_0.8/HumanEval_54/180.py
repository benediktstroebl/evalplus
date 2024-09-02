

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

    chars0 = {}
    chars1 = {}

    for i in range(len(s0)):
        if s0[i] in chars0:
            chars0[s0[i]] += 1
        else:
            chars0[s0[i]] = 1
        if s1[i] in chars1:
            chars1[s1[i]] += 1
        else:
            chars1[s1[i]] = 1

    if chars0 != chars1:
        return False
    return True

