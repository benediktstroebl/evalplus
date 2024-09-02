

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

    """
    s1 = sorted(s1)
    for i in range(len(s0)):
        if s1[i] != s0[i]:
            return False
    return True
    """

    l0 = len(s0)
    l1 = len(s1)
    if l0 != l1:
        return False

    arr = [0] * 26
    for s in s0 + s1:
        arr[ord(s) - ord("a")] += 1

    for i in range(26):
        if arr[i] != 0:
            return False
    return True
