

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

    # s0 = list(s0)
    # s1 = list(s1)
    #
    # for i in s0:
    #     if i not in s1:
    #         return False
    # for j in s1:
    #     if j not in s0:
    #         return False
    # return True

    # return sorted(s0) == sorted(s1)

    # return sorted(s0) == sorted(s1) or sorted(s1) == sorted(s0)

    return sorted(s0) == sorted(s1) or sorted(s1) == sorted(s0)

