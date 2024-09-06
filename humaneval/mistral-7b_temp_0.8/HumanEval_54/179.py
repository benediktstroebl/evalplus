

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
    n_0 = len(s0)
    n_1 = len(s1)

    if n_0 == n_1:
        d = {}
        for i in range(n_0):
            if s0[i] not in d:
                d[s0[i]] = 1
            else:
                d[s0[i]] += 1

        for i in range(n_1):
            if s1[i] not in d or d[s1[i]] == 0:
                return False
            else:
                d[s1[i]] -= 1

        return True
    else:
        return False

